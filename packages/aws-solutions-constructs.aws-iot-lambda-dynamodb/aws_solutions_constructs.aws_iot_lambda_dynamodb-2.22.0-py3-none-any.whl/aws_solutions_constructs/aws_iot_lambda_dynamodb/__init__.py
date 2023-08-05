'''
# aws-iot-lambda-dynamodb module

<!--BEGIN STABILITY BANNER-->---


![Stability: Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

> All classes are under active development and subject to non-backward compatible changes or removal in any
> future version. These are not subject to the [Semantic Versioning](https://semver.org/) model.
> This means that while you may use them, you may need to update your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

| **Reference Documentation**:| <span style="font-weight: normal">https://docs.aws.amazon.com/solutions/latest/constructs/</span>|
|:-------------|:-------------|

<div style="height:8px"></div>

| **Language**     | **Package**        |
|:-------------|-----------------|
|![Python Logo](https://docs.aws.amazon.com/cdk/api/latest/img/python32.png) Python|`aws_solutions_constructs.aws_iot_lambda_dynamodb`|
|![Typescript Logo](https://docs.aws.amazon.com/cdk/api/latest/img/typescript32.png) Typescript|`@aws-solutions-constructs/aws-iot-lambda-dynamodb`|
|![Java Logo](https://docs.aws.amazon.com/cdk/api/latest/img/java32.png) Java|`software.amazon.awsconstructs.services.iotlambdadynamodb`|

## Overview

This AWS Solutions Construct implements an AWS IoT topic rule, an AWS Lambda function and Amazon DynamoDB table with the least privileged permissions.

Here is a minimal deployable pattern definition:

Typescript

```python
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { IotToLambdaToDynamoDBProps, IotToLambdaToDynamoDB } from '@aws-solutions-constructs/aws-iot-lambda-dynamodb';
import * as lambda from 'aws-cdk-lib/aws-lambda';

const constructProps: IotToLambdaToDynamoDBProps = {
  lambdaFunctionProps: {
      code: lambda.Code.fromAsset(`lambda`),
      runtime: lambda.Runtime.NODEJS_14_X,
      handler: 'index.handler'
  },
  iotTopicRuleProps: {
      topicRulePayload: {
          ruleDisabled: false,
          description: "Processing of DTC messages from the AWS Connected Vehicle Solution.",
          sql: "SELECT * FROM 'connectedcar/dtc/#'",
          actions: []
      }
  }
};

new IotToLambdaToDynamoDB(this, 'test-iot-lambda-dynamodb-stack', constructProps);
```

Python

```python
from aws_solutions_constructs.aws_iot_lambda_dynamodb import IotToLambdaToDynamoDB
from aws_cdk import (
    aws_iot as iot,
    aws_lambda as _lambda,
    Stack
)
from constructs import Construct

IotToLambdaToDynamoDB(self, 'test-iot-lambda-dynamodb-stack',
            lambda_function_props=_lambda.FunctionProps(
                code=_lambda.Code.from_asset('lambda'),
                runtime=_lambda.Runtime.PYTHON_3_9,
                handler='index.handler'
            ),
            iot_topic_rule_props=iot.CfnTopicRuleProps(
                topic_rule_payload=iot.CfnTopicRule.TopicRulePayloadProperty(
                    rule_disabled=False,
                    description="Processing of DTC messages from the AWS Connected Vehicle Solution.",
                    sql="SELECT * FROM 'connectedcar/dtc/#'",
                    actions=[]
                )
            ))
```

Java

```java
import software.constructs.Construct;
import java.util.List;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.lambda.*;
import software.amazon.awscdk.services.lambda.Runtime;
import software.amazon.awscdk.services.iot.*;
import software.amazon.awscdk.services.iot.CfnTopicRule.TopicRulePayloadProperty;
import software.amazon.awsconstructs.services.iotlambdadynamodb.*;

new IotToLambdaToDynamoDB(this, "test-iot-lambda-dynamodb-stack", new IotToLambdaToDynamoDBProps.Builder()
        .lambdaFunctionProps(new FunctionProps.Builder()
                .runtime(Runtime.NODEJS_14_X)
                .code(Code.fromAsset("lambda"))
                .handler("index.handler")
                .build())
        .iotTopicRuleProps(new CfnTopicRuleProps.Builder()
                .topicRulePayload(new TopicRulePayloadProperty.Builder()
                        .ruleDisabled(false)
                        .description("Processing of DTC messages from the AWS Connected Vehicle Solution.")
                        .sql("SELECT * FROM 'connectedcar/dtc/#'")
                        .actions(List.of())
                        .build())
                .build())
        .build());
```

## Pattern Construct Props

| **Name**     | **Type**        | **Description** |
|:-------------|:----------------|-----------------|
|existingLambdaObj?|[`lambda.Function`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-lambda.Function.html)|Existing instance of Lambda Function object, providing both this and `lambdaFunctionProps` will cause an error.|
|lambdaFunctionProps?|[`lambda.FunctionProps`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-lambda.FunctionProps.html)|User provided props to override the default props for the Lambda function.|
|iotTopicRuleProps|[`iot.CfnTopicRuleProps`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-iot.CfnTopicRuleProps.html)|User provided props to override the default props|
|dynamoTableProps?|[`dynamodb.TableProps`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-dynamodb.TableProps.html)|Optional user provided props to override the default props for DynamoDB Table|
|tablePermissions?|`string`|Optional table permissions to grant to the Lambda function. One of the following may be specified: `All`, `Read`, `ReadWrite`, `Write`.|

## Pattern Properties

| **Name**     | **Type**        | **Description** |
|:-------------|:----------------|-----------------|
|iotTopicRule|[`iot.CfnTopicRule`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-iot.CfnTopicRule.html)|Returns an instance of iot.CfnTopicRule created by the construct|
|lambdaFunction|[`lambda.Function`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-lambda.Function.html)|Returns an instance of lambda.Function created by the construct|
|dynamoTable|[`dynamodb.Table`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-dynamodb.Table.html)|Returns an instance of dynamodb.Table created by the construct|

## Default settings

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon IoT Rule

* Configure least privilege access IAM role for Amazon IoT

### AWS Lambda Function

* Configure limited privilege access IAM role for Lambda function
* Enable reusing connections with Keep-Alive for NodeJs Lambda function
* Enable X-Ray Tracing
* Set Environment Variables

  * AWS_NODEJS_CONNECTION_REUSE_ENABLED (for Node 10.x and higher functions)

### Amazon DynamoDB Table

* Set the billing mode for DynamoDB Table to On-Demand (Pay per request)
* Enable server-side encryption for DynamoDB Table using AWS managed KMS Key
* Creates a partition key called 'id' for DynamoDB Table
* Retain the Table when deleting the CloudFormation stack
* Enable continuous backups and point-in-time recovery

## Architecture

![Architecture Diagram](architecture.png)

---


© Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk.aws_dynamodb
import aws_cdk.aws_iot
import aws_cdk.aws_lambda
import constructs


class IotToLambdaToDynamoDB(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-solutions-constructs/aws-iot-lambda-dynamodb.IotToLambdaToDynamoDB",
):
    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        iot_topic_rule_props: typing.Union[aws_cdk.aws_iot.CfnTopicRuleProps, typing.Dict[str, typing.Any]],
        dynamo_table_props: typing.Optional[typing.Union[aws_cdk.aws_dynamodb.TableProps, typing.Dict[str, typing.Any]]] = None,
        existing_lambda_obj: typing.Optional[aws_cdk.aws_lambda.Function] = None,
        lambda_function_props: typing.Optional[typing.Union[aws_cdk.aws_lambda.FunctionProps, typing.Dict[str, typing.Any]]] = None,
        table_permissions: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: - represents the scope for all the resources.
        :param id: - this is a a scope-unique id.
        :param iot_topic_rule_props: User provided props to override the default props. Default: - Default props are used
        :param dynamo_table_props: Optional user provided props to override the default props. Default: - Default props are used
        :param existing_lambda_obj: Existing instance of Lambda Function object, providing both this and ``lambdaFunctionProps`` will cause an error. Default: - None
        :param lambda_function_props: User provided props to override the default props for the Lambda function. Default: - Default props are used
        :param table_permissions: Optional table permissions to grant to the Lambda function. One of the following may be specified: "All", "Read", "ReadWrite", "Write". Default: - Read/write access is given to the Lambda function if no value is specified.

        :access: public
        :since: 0.8.0
        :summary: Constructs a new instance of the IotToLambdaToDynamoDB class.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IotToLambdaToDynamoDB.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = IotToLambdaToDynamoDBProps(
            iot_topic_rule_props=iot_topic_rule_props,
            dynamo_table_props=dynamo_table_props,
            existing_lambda_obj=existing_lambda_obj,
            lambda_function_props=lambda_function_props,
            table_permissions=table_permissions,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="dynamoTable")
    def dynamo_table(self) -> aws_cdk.aws_dynamodb.Table:
        return typing.cast(aws_cdk.aws_dynamodb.Table, jsii.get(self, "dynamoTable"))

    @builtins.property
    @jsii.member(jsii_name="iotTopicRule")
    def iot_topic_rule(self) -> aws_cdk.aws_iot.CfnTopicRule:
        return typing.cast(aws_cdk.aws_iot.CfnTopicRule, jsii.get(self, "iotTopicRule"))

    @builtins.property
    @jsii.member(jsii_name="lambdaFunction")
    def lambda_function(self) -> aws_cdk.aws_lambda.Function:
        return typing.cast(aws_cdk.aws_lambda.Function, jsii.get(self, "lambdaFunction"))


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/aws-iot-lambda-dynamodb.IotToLambdaToDynamoDBProps",
    jsii_struct_bases=[],
    name_mapping={
        "iot_topic_rule_props": "iotTopicRuleProps",
        "dynamo_table_props": "dynamoTableProps",
        "existing_lambda_obj": "existingLambdaObj",
        "lambda_function_props": "lambdaFunctionProps",
        "table_permissions": "tablePermissions",
    },
)
class IotToLambdaToDynamoDBProps:
    def __init__(
        self,
        *,
        iot_topic_rule_props: typing.Union[aws_cdk.aws_iot.CfnTopicRuleProps, typing.Dict[str, typing.Any]],
        dynamo_table_props: typing.Optional[typing.Union[aws_cdk.aws_dynamodb.TableProps, typing.Dict[str, typing.Any]]] = None,
        existing_lambda_obj: typing.Optional[aws_cdk.aws_lambda.Function] = None,
        lambda_function_props: typing.Optional[typing.Union[aws_cdk.aws_lambda.FunctionProps, typing.Dict[str, typing.Any]]] = None,
        table_permissions: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param iot_topic_rule_props: User provided props to override the default props. Default: - Default props are used
        :param dynamo_table_props: Optional user provided props to override the default props. Default: - Default props are used
        :param existing_lambda_obj: Existing instance of Lambda Function object, providing both this and ``lambdaFunctionProps`` will cause an error. Default: - None
        :param lambda_function_props: User provided props to override the default props for the Lambda function. Default: - Default props are used
        :param table_permissions: Optional table permissions to grant to the Lambda function. One of the following may be specified: "All", "Read", "ReadWrite", "Write". Default: - Read/write access is given to the Lambda function if no value is specified.

        :summary: The properties for the IotToLambdaToDynamoDB class.
        '''
        if isinstance(iot_topic_rule_props, dict):
            iot_topic_rule_props = aws_cdk.aws_iot.CfnTopicRuleProps(**iot_topic_rule_props)
        if isinstance(dynamo_table_props, dict):
            dynamo_table_props = aws_cdk.aws_dynamodb.TableProps(**dynamo_table_props)
        if isinstance(lambda_function_props, dict):
            lambda_function_props = aws_cdk.aws_lambda.FunctionProps(**lambda_function_props)
        if __debug__:
            type_hints = typing.get_type_hints(IotToLambdaToDynamoDBProps.__init__)
            check_type(argname="argument iot_topic_rule_props", value=iot_topic_rule_props, expected_type=type_hints["iot_topic_rule_props"])
            check_type(argname="argument dynamo_table_props", value=dynamo_table_props, expected_type=type_hints["dynamo_table_props"])
            check_type(argname="argument existing_lambda_obj", value=existing_lambda_obj, expected_type=type_hints["existing_lambda_obj"])
            check_type(argname="argument lambda_function_props", value=lambda_function_props, expected_type=type_hints["lambda_function_props"])
            check_type(argname="argument table_permissions", value=table_permissions, expected_type=type_hints["table_permissions"])
        self._values: typing.Dict[str, typing.Any] = {
            "iot_topic_rule_props": iot_topic_rule_props,
        }
        if dynamo_table_props is not None:
            self._values["dynamo_table_props"] = dynamo_table_props
        if existing_lambda_obj is not None:
            self._values["existing_lambda_obj"] = existing_lambda_obj
        if lambda_function_props is not None:
            self._values["lambda_function_props"] = lambda_function_props
        if table_permissions is not None:
            self._values["table_permissions"] = table_permissions

    @builtins.property
    def iot_topic_rule_props(self) -> aws_cdk.aws_iot.CfnTopicRuleProps:
        '''User provided props to override the default props.

        :default: - Default props are used
        '''
        result = self._values.get("iot_topic_rule_props")
        assert result is not None, "Required property 'iot_topic_rule_props' is missing"
        return typing.cast(aws_cdk.aws_iot.CfnTopicRuleProps, result)

    @builtins.property
    def dynamo_table_props(self) -> typing.Optional[aws_cdk.aws_dynamodb.TableProps]:
        '''Optional user provided props to override the default props.

        :default: - Default props are used
        '''
        result = self._values.get("dynamo_table_props")
        return typing.cast(typing.Optional[aws_cdk.aws_dynamodb.TableProps], result)

    @builtins.property
    def existing_lambda_obj(self) -> typing.Optional[aws_cdk.aws_lambda.Function]:
        '''Existing instance of Lambda Function object, providing both this and ``lambdaFunctionProps`` will cause an error.

        :default: - None
        '''
        result = self._values.get("existing_lambda_obj")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.Function], result)

    @builtins.property
    def lambda_function_props(
        self,
    ) -> typing.Optional[aws_cdk.aws_lambda.FunctionProps]:
        '''User provided props to override the default props for the Lambda function.

        :default: - Default props are used
        '''
        result = self._values.get("lambda_function_props")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.FunctionProps], result)

    @builtins.property
    def table_permissions(self) -> typing.Optional[builtins.str]:
        '''Optional table permissions to grant to the Lambda function.

        One of the following may be specified: "All", "Read", "ReadWrite", "Write".

        :default: - Read/write access is given to the Lambda function if no value is specified.
        '''
        result = self._values.get("table_permissions")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotToLambdaToDynamoDBProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IotToLambdaToDynamoDB",
    "IotToLambdaToDynamoDBProps",
]

publication.publish()
