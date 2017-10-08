def get_response_dict(es_response):
    """
    Serialize every search hit to a dictionary
    :param es_response: returning response
    :return:
    """
    return [hit.to_dict() for hit in es_response.hits]
