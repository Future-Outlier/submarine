# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

# flake8: noqa

"""
    Submarine API

    The Submarine REST API allows you to access Submarine resources such as,  experiments, environments and notebooks. The  API is hosted under the /v1 path on the Submarine server. For example,  to list experiments on a server hosted at http://localhost:8080, access http://localhost:8080/api/v1/experiment/  # noqa: E501

    The version of the OpenAPI document: 0.7.0-SNAPSHOT
    Contact: dev@submarine.apache.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "0.7.0-SNAPSHOT"

# import apis into sdk package
from submarine.client.api.environment_api import EnvironmentApi
from submarine.client.api.experiment_api import ExperimentApi
from submarine.client.api.notebook_api import NotebookApi

# import ApiClient
from submarine.client.api_client import ApiClient
from submarine.client.configuration import Configuration
from submarine.client.exceptions import (
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    OpenApiException,
)

# import models into sdk package
from submarine.client.models.code_spec import CodeSpec
from submarine.client.models.environment_spec import EnvironmentSpec
from submarine.client.models.experiment_meta import ExperimentMeta
from submarine.client.models.experiment_spec import ExperimentSpec
from submarine.client.models.experiment_task_spec import ExperimentTaskSpec
from submarine.client.models.experiment_template_submit import ExperimentTemplateSubmit
from submarine.client.models.json_response import JsonResponse
from submarine.client.models.kernel_spec import KernelSpec
from submarine.client.models.notebook_meta import NotebookMeta
from submarine.client.models.notebook_pod_spec import NotebookPodSpec
from submarine.client.models.notebook_spec import NotebookSpec