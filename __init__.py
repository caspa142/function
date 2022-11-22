import logging

import azure.functions as func

from . import integration as ig

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    lower = req.route_params.get('lower')
    upper = req.route_params.get('upper')
    
    result = ""
    for i in subintervals:
        j = integral(fn, i, float(lower), float(upper))
        result += "<p> i=" + str(i) + ": " + str(j) + "</p>"
    return func.HttpResponse(
        result,
        status_code=200,
        mimetype='text/html'
        )
