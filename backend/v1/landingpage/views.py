import collections
import time
import boto3
from functools import wraps

from decouple import config
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action, renderer_classes
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.response import Response
from rest_framework.utils import json

import v1.permissions as custom_permissions
from v1.landingpage.models import LandingPage as LandingModel
from v1.landingpage.utils import LandingPage as LandingGenerator


# def response_decorator():
#     def wrapper(func):
#         @wraps(func)
#         def decorator(*args, **kwargs):
#             data = func(*args, **kwargs)
#             response_formatter = ReturnValuesFormatter()
#
#             response_formatter.values_to_return = {
#                 'state': data['state'],
#                 'data': data['data'],
#                 'message': data['message'],
#                 'options': data['options']
#             }
#             return Response(**response_formatter.generate())
#
#         return decorator
#
#     return wrapper

def response_decorator(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        data = func(*args, **kwargs)
        response_formatter = ReturnValuesFormatter()

        response_formatter.values_to_return = {
            'state': data['state'],
            'data': data['data'],
            'message': data['message'],
            'options': data['options']
        }
        return Response(**response_formatter.generate())

    return decorator


class ReturnValuesFormatter:
    def __init__(self):
        self._values_to_return = None

    @property
    def values_to_return(self):
        return self._values_to_return

    @values_to_return.setter
    def values_to_return(self, set_values):
        values_to_return_named_tuple = collections.namedtuple('values_to_return',
                                                              ['state',
                                                               'data',
                                                               'message',
                                                               'options'])
        self._values_to_return = values_to_return_named_tuple(**set_values)

    def generate(self):
        formatted_values = {
            'data':
                {
                    'state': self._values_to_return.state,
                    'data': self._values_to_return.data,
                    'message': self._values_to_return.message
                }
        }
        formatted_values.update(self._values_to_return.options)
        return formatted_values


class LandingPageViewSetsUtils(viewsets.ViewSet):
    landing_pages_model = LandingModel(choice_db='infomagazine')
    permission_classes = (custom_permissions.IsMarketer,)
    return_value_formatter = ReturnValuesFormatter

    def get_landing_data(self, landing_detail=None, is_generate=False):
        if landing_detail['state']:
            landing_pages = LandingGenerator(landing_detail['data']['landing_info'], is_generate=is_generate)
            lading_page_generated = landing_pages.generate()
            lading_page_generated.update(
                {'options': {'status': status.HTTP_200_OK} if landing_detail['state'] else {
                    'status': status.HTTP_500_INTERNAL_SERVER_ERROR}})
            return lading_page_generated
        else:
            landing_detail.update({'options': {'status': status.HTTP_200_OK} if landing_detail['state'] else {
                'status': status.HTTP_404_NOT_FOUND}})
            return landing_detail


class LandingPageViewSets(LandingPageViewSetsUtils):
    @response_decorator
    def list(self, request):
        projection = {'_id': 1, 'landing_info.landing.name': 1, 'landing_info.landing.views': 1}
        response_data = self.landing_pages_model.list(choice_collection='landing_pages', projection=projection)
        response_data.update({"options": {'status': status.HTTP_200_OK} if response_data['state'] else {
            'status': status.HTTP_404_NOT_FOUND}})
        return response_data

    @response_decorator
    def create(self, request):
        body = json.loads(request.body)
        document = {
            "company_id": body['company_id'],
            "landing_info": body['landing_info'],
            "updated_date": body['updated_date']
        }
        response_data = self.landing_pages_model.create(choice_collection='landing_pages', document=document)
        response_data.update({"options": {'status': status.HTTP_201_CREATED} if response_data['state'] else {
            'status': status.HTTP_503_SERVICE_UNAVAILABLE}})
        return response_data

    @response_decorator
    def retrieve(self, request, pk):
        response_data = self.landing_pages_model.retrieve(choice_collection='landing_pages', doc_id=pk)
        response_data.update({"options": {'status': status.HTTP_200_OK} if response_data['state'] else {
            'status': status.HTTP_404_NOT_FOUND}})
        return response_data

    @response_decorator
    def update(self, request, pk):
        response_data = self.landing_pages_model.update(choice_collection='landing_pages', doc_id=pk,
                                                        data_to_update={'$set': request.data})
        response_data.update({"options": {'status': status.HTTP_200_OK} if response_data['state'] else {
            'status': status.HTTP_404_NOT_FOUND}})
        return response_data

    @response_decorator
    def destroy(self, request, pk):
        response_data = self.landing_pages_model.destroy(choice_collection='landing_pages', doc_id=pk)
        response_data.update({"options": {'status': status.HTTP_204_NO_CONTENT} if response_data['state'] else {
            'status': status.HTTP_404_NOT_FOUND}})
        return response_data

    @action(detail=True)
    @response_decorator
    def preview(self, request, pk):
        get_detail = self.retrieve(request, pk)
        response_data = self.get_landing_data(landing_detail=get_detail.data)
        return response_data

    @action(detail=True, renderer_classes=[StaticHTMLRenderer], permission_classes=[permissions.AllowAny])
    def test_preview(self, request, pk):
        get_detail = self.retrieve(request, pk)
        response_data = self.get_landing_data(landing_detail=get_detail.data)
        return Response(response_data['data'])

    @action(detail=True, methods=['GET', 'POST'])
    @response_decorator
    def landing_urls(self, request, pk):
        s3_client = boto3.client(
            's3',
            aws_access_key_id=config('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY'),
            region_name='ap-northeast-2'
        )
        if request.method == 'GET':
            s3_response = s3_client.list_objects(Bucket=config('AWS_STORAGE_BUCKET_NAME'),
                                                 Prefix='landings/' + pk + '/')
            if s3_response['ResponseMetadata']['HTTPStatusCode'] == 200:
                url_list_do_handling = [url['Key'].replace('landings/', 'https://landings.infomagazine.xyz/') for url in
                                        s3_response.get('Contents', []) if url]
                return {'state': True, 'data': url_list_do_handling, 'message': 'Succeed.',
                        'options': {'status': status.HTTP_200_OK}}
            else:
                return {'state': False, 'data': '', 'message': 'Failed.',
                        'options': {'status': status.HTTP_500_INTERNAL_SERVER_ERROR}}

        elif request.method == 'POST':
            get_detail = self.retrieve(request, pk)
            response_data = self.get_landing_data(landing_detail=get_detail.data, is_generate=True)
            landing_id = get_detail.data['data']['_id']['$oid']
            landing_base_url = get_detail.data['data']['landing_info']['landing']['base_url']
            epoch_time = time.time()
            landing_url = f'''landings/{landing_id}/{landing_base_url}_{str(int(epoch_time))}.html'''
            s3_response_data = s3_client.put_object(Body=response_data['data'],
                                                    Bucket=config('AWS_STORAGE_BUCKET_NAME'),
                                                    Key=landing_url,
                                                    ContentType='text/html')
            if s3_response_data['ResponseMetadata']['HTTPStatusCode'] == 200:
                return {'state': True, 'data': landing_url, 'message': 'Succeed.',
                        'options': {'status': status.HTTP_200_OK}}
            else:
                return {'state': False, 'data': '', 'message': 'Failed.',
                        'options': {'status': status.HTTP_500_INTERNAL_SERVER_ERROR}}

    @action(detail=True, methods=['DELETE'], url_path='landing_urls/(?P<landing_url>[^/.]+)')
    @response_decorator
    def landing_urls_detail(self, request, pk, landing_url):
        if request.method == 'DELETE':
            s3_client = boto3.client(
                's3',
                aws_access_key_id=config('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY'),
                region_name='ap-northeast-2'
            )
            s3_response = s3_client.delete_object(Bucket=config('AWS_STORAGE_BUCKET_NAME'),
                                                  Key='landings/' + pk + '/' + landing_url + '.html')
            if s3_response['ResponseMetadata']['HTTPStatusCode'] == 204:
                return {'state': True, 'data': landing_url, 'message': 'Succeed.',
                        'options': {'status': status.HTTP_204_NO_CONTENT}}
            else:
                return {'state': False, 'data': '', 'message': 'Failed.',
                        'options': {'status': status.HTTP_500_INTERNAL_SERVER_ERROR}}
