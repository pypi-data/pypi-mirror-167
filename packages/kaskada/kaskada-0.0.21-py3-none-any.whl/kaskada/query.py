"""
Copyright (C) 2022 Kaskada Inc. All rights reserved.

This package cannot be used, copied or distributed without the express
written permission of Kaskada Inc.

For licensing inquiries, please contact us at info@kaskada.com.
"""

from kaskada.client import Client
import kaskada

import grpc


def get_query(query_id: str, client: Client = None):
    """
    Gets a query by query ID
    Args:
        query_id (str): The target query ID
        client (Client, optional): The Kaskada Client. Defaults to kaskada.KASKADA_DEFAULT_CLIENT.

    Raises:
        NotImplementedError
    """
    if client is None:
        client = kaskada.KASKADA_DEFAULT_CLIENT

    try:
        kaskada.validate_client(client)
        # TODO: Call the service once implemented
        raise NotImplementedError()
    except grpc.RpcError as e:
        kaskada.handleGrpcError(e)
    except Exception as e:
        kaskada.handleException(e)


def list_queries(search: str, client: Client = None):
    """
    Lists all queries the user has previously performed

    Args:
        search (str): The search parameter to filter queries by. Defaults to None.
        client (Client, optional): The Kaskada Client. Defaults to kaskada.KASKADA_DEFAULT_CLIENT.

    Raises:
        NotImplementedError
    """
    if client is None:
        client = kaskada.KASKADA_DEFAULT_CLIENT

    try:
        kaskada.validate_client(client)
        # TODO: Call the service once implemented
        raise NotImplementedError()
    except grpc.RpcError as e:
        kaskada.handleGrpcError(e)
    except Exception as e:
        kaskada.handleException(e)
