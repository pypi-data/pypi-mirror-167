"""
This script provides the `Hub` class to communicate with Watchful Hub, interface
with your custom data enrichment functions and models, and perform data
enrichment on your datasets that can then be added to your Watchful projects.
"""
################################################################################


import datetime
import http.client
import json
import os
import sys
from typing import Dict, Optional
from watchful import client, attributes
from watchful.enricher import Enricher

THIS_FILE_DIR = os.path.dirname(os.path.abspath(__file__))


class Hub:
    """
    `Hub` provides methods to interact with Watchful Hub and stores the state
    about the client's access to hub. For example, once the client has logged in
    to Watchful Hub, `Hub` will store the retrieved auth token.
    """

    __host: Optional[str] = None
    __port: Optional[str] = None
    __credentials: Optional[str] = None
    __token: Optional[str] = None
    __datasets_dir: Optional[str] = None

    def __init__(
        self,
        credentials: Optional[str] = None,
        host: Optional[str] = None,
        port: Optional[str] = None) -> None:
        """
        The user must login on `Hub` initialization in order to retrieve the
        auth token needed for all other hub actions.
        """
        if host is not None and port is not None:
            self.__host = host
            self.__port = port
        elif host is None and port is None:
            self.__host = "34.127.106.236"
            self.__port = "9005"
        else:
            raise ValueError(
                "Both host and port must be strings, or both omitted to use "
                "the defaults."
            )

        self.__credentials = credentials
        self.__setup()


    def __setup(self) -> None:
        user_home_path = os.path.expanduser("~")
        datasets_dir = os.path.join(user_home_path, "datasets")
        os.makedirs(datasets_dir, exist_ok=True)
        self.__datasets_dir = datasets_dir


    def login(self, credentials: Optional[str] = None) -> str:
        if credentials:
            self.__credentials = credentials
        response = self.__hub_api("login", credentials=self.__credentials)
        self.__set_token(response)
        return response


    def __hub_api(
        self,
        verb: str,
        **action: Dict[str, str]) -> str:
        """
        Convenience method for Watchful Hub / collaboration API calls.
        """
        headers = {"Content-Type": "application/json"}
        if verb != "login":
            headers.update({"Authorization": f"Bearer {self.__token}"})
        action["verb"] = verb
        # Amend this for connecting from another IP to Hub IP.
        # conn = client._get_conn()

        conn = self.__get_conn()
        conn.request(
            "POST",
            "/remote",
            json.dumps(action),
            headers
        )
        return client._read_response_summary(conn.getresponse())


    def __get_conn(self) -> http.client.HTTPConnection:
        return http.client.HTTPConnection(f"{self.__host}:{self.__port}")


    def __set_token(
        self,
        response: str) -> None:
        if "token" in response:
            self.__token = response["token"]
        else:
            self.__token = None
            raise ValueError("Watchful Hub did not return an auth token!")


    def __is_token_set(self) -> None:
        if not self.__token:
            raise ValueError("You have yet to login to Watchful Hub!")


    def __get_dataset_id(
        self,
        project_name: str) -> str:
        """
        Function to get `dataset_id`. There should be a user-friendly string,
        such as the `project_name`, that the user can use to query hub for the
        `dataset_id`.
        """
        self.__is_token_set()

        # This could be one way for the api, depending on how the final hub api is
        # engineered. Assumes that we always use the last (most recent) dataset.
        # TODO: Check if and how there can be more than 1 dataset for a project.
        resp = self.get()
        dataset_id = resp["projects"][project_name]["dataset_ids"][-1]
        return dataset_id


    def get(self) -> str:
        return self.__hub_api("nop")


    def __get_dataset_filepath(
        self,
        dataset_id: str) -> str:
        """
        Function to get the `dataset` using the `dataset_id` and save `dataset`
        to disk.
        """
        self.__is_token_set()

        # This could be one way for the api, depending on how the final hub api is
        # engineered.
        action = {"dataset_id": dataset_id}
        conn = self.__get_conn()
        conn.request(
            "GET",
            "/datasets",
            json.dumps(action),
            {"Content-Type": "text/csv"}
        )
        resp = conn.getresponse()
        assert 200 == int(resp.status)

        dataset_filepath = os.path.join(self.__datasets_dir, f"{dataset_id}.csv")

        with open(dataset_filepath, "wb") as f:
            for line in resp:
                f.write(line)

        return dataset_filepath


    @staticmethod
    def __create_attributes_filepath(
        filepath: str) -> str:
        """
        Function to append timestamp to an attributes filename, so the machine
        where the data enrichment is performed can keep snapshots of attributes
        of the same dataset. The format of `timestamp` is
        <YYYY-MM-DD_HH-MM-SS-SSSSSS>.
        """
        timestamp = (
            str(datetime.datetime.now())
            .replace(" ", "_")
            .replace(":", "-")
            .replace(".", "-")
        )
        ext = "attrs"

        filepath_noext, _ = os.path.splitext(filepath)
        filepath_ts_attrs = f"{filepath_noext}__{timestamp}.{ext}"
        return filepath_ts_attrs


    def enrich_dataset(
        self,
        project_name: str,
        custom_enricher_cls: Enricher,
        dataset_filepath: str,
        attributes_filepath: str) -> str:
        """
        Function to enrich data.
        """
        # test_dir_path = os.path.join(
        #     os.path.dirname(os.path.dirname(THIS_FILE_DIR)),
        #     "tests"
        # )
        # attributes_filepath = self.__append_timestamp(attributes_filepath)
        # attributes.enrich(
        #     os.path.join(test_dir_path, dataset_filepath),
        #     os.path.join(test_dir_path, attributes_filepath),
        #     custom_enricher.enrich_row,
        #     custom_enricher.enrichment_args,
        # )

        dataset_id = self.__get_dataset_id(project_name)
        dataset_filepath = self.__get_dataset_filepath(dataset_id)
        attributes_filepath = self.__create_attributes_filepath(
            dataset_filepath
        )
        custom_enricher = custom_enricher_cls()

        attributes.set_multiprocessing(False)
        attributes.enrich(
            dataset_filepath,
            attributes_filepath,
            custom_enricher.enrich_row,
            custom_enricher.enrichment_args,
        )

        return self.__send_attributes_to_hub(
            dataset_id,
            attributes_filepath
        )


    def __send_attributes_to_hub(
        self,
        dataset_id: str,
        attributes_filepath: str) -> str:
        """
        Function to send attributes (enriched data) to `Hub`. In `Hub`,
        minimally the token should be verified with accessing the dataset of the
        `dataset_id`. `Hub` should then push down the attributes to all clients
        (users) of the project.
        TODO: Check if besides `dataset_id`, `project_id` is also needed.
        """
        self.__is_token_set()

        # Example 1:
        # curl -iX PUT \
        #   --url 'http://34.127.106.236:9005/fs/default/datasets/attrs/test_dataset_0001' \
        #   -H 'Content-Type: text/plain' \
        #   -H "Authorization: Bearer <TOKEN>" \
        #   -d 'test_data_0001'
        # Example 2:
        # conn = self.__get_conn()
        # conn.request(
        #     "PUT",
        #     f"/fs/default/datasets/attrs/{dataset_id}/"
        #     f"{os.path.basename(attributes_filepath)}",
        #     open(attributes_filepath, "r"),
        #     {
        #         "Content-Type": "text/plain",
        #         "Authorization": f"Bearer {self.__token}",
        #     },
        # )
        return self.__hub_api(
            "attributes",
            id=dataset_id,
            attrs_id=os.path.basename(attributes_filepath),
            file=open(
                attributes_filepath,
                "r",
                encoding=sys.getdefaultencoding()
            ).read()
        )

    # Migrated from `client.py`
    # def publish(self) -> str:
    #     self.__is_token_set()
    #     return self.__hub_api("publish")

    # def fetch(self) -> str:
    #     self.__is_token_set()
    #     return self.__hub_api("fetch")

    # def pull(self) -> str:
    #     self.__is_token_set()
    #     return self.__hub_api("pull")

    # def push(self) -> str:
    #     self.__is_token_set()
    #     return self.__hub_api("push")

    # def peek(self) -> str:
    #     self.__is_token_set()
    #     return self.__hub_api("peek")


# def send_request(verb, endpoint, payload, addedheaders={}):
#     headers = {"Content-Type": "application/json"}
#     headers.update(addedheaders)
#     conn = http.client.HTTPConnection(hub_host + ":" + hub_port)
#     conn.request(verb, endpoint, json.dumps(payload), headers)
#     return conn.getresponse()

# def read_response_body(resp, is_json=False):
#     body = resp.read()
#     if is_json:
#         body = json.loads(body)
#     return body
