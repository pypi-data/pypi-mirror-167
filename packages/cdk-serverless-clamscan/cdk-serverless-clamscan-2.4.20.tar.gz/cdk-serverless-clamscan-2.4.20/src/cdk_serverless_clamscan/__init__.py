'''
# cdk-serverless-clamscan

[![npm version](https://badge.fury.io/js/cdk-serverless-clamscan.svg)](https://badge.fury.io/js/cdk-serverless-clamscan)
[![PyPI version](https://badge.fury.io/py/cdk-serverless-clamscan.svg)](https://badge.fury.io/py/cdk-serverless-clamscan)

An [aws-cdk](https://github.com/aws/aws-cdk) construct that uses [ClamAV®](https://www.clamav.net/) to scan objects in Amazon S3 for viruses. The construct provides a flexible interface for a system to act based on the results of a ClamAV virus scan. Check out this [blogpost](https://aws.amazon.com/blogs/developer/virus-scan-s3-buckets-with-a-serverless-clamav-based-cdk-construct/) for a guided walkthrough.

![Overview](serverless-clamscan.png)

## Pre-Requisites

**Docker:** The ClamAV Lambda functions utilizes a [container image](https://aws.amazon.com/blogs/aws/new-for-aws-lambda-container-image-support/) that is built locally using [docker bundling](https://aws.amazon.com/blogs/devops/building-apps-with-aws-cdk/)

## Examples

This project uses [projen](https://github.com/projen/projen) and thus all the constructs follow language specific standards and naming patterns. For more information on how to translate the following examples into your desired language read the CDK guide on [Translating TypeScript AWS CDK code to other languages](https://docs.aws.amazon.com/cdk/latest/guide/multiple_languages.html)

### Example 1. (Default destinations with rule target)

<details><summary>typescript</summary>
<p>

```python
import { RuleTargetInput } from 'aws-cdk-lib/aws-events';
import { SnsTopic } from 'aws-cdk-lib/aws-events-targets';
import { Bucket } from 'aws-cdk-lib/aws-s3';
import { Topic } from 'aws-cdk-lib/aws-sns';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { ServerlessClamscan } from 'cdk-serverless-clamscan';

export class CdkTestStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const bucket_1 = new Bucket(this, 'rBucket1');
    const bucket_2 = new Bucket(this, 'rBucket2');
    const bucketList = [bucket_1, bucket_2];
    const sc = new ServerlessClamscan(this, 'rClamscan', {
      buckets: bucketList,
    });
    const bucket_3 = new Bucket(this, 'rBucket3');
    sc.addSourceBucket(bucket_3);
    const infectedTopic = new Topic(this, 'rInfectedTopic');
    sc.infectedRule?.addTarget(
      new SnsTopic(infectedTopic, {
        message: RuleTargetInput.fromEventPath(
          '$.detail.responsePayload.message',
        ),
      }),
    );
  }
}
```

</p>
</details><details><summary>python</summary>
<p>

```python
from aws_cdk import (
  Stack,
  aws_events as events,
  aws_events_targets as events_targets,
  aws_s3 as s3,
  aws_sns as sns
)
from cdk_serverless_clamscan import ServerlessClamscan
from constructs import Construct

class CdkTestStack(Stack):

  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    bucket_1 = s3.Bucket(self, "rBucket1")
    bucket_2 = s3.Bucket(self, "rBucket2")
    bucketList = [ bucket_1, bucket_2 ]
    sc = ServerlessClamscan(self, "rClamScan",
      buckets=bucketList,
    )
    bucket_3 = s3.Bucket(self, "rBucket3")
    sc.add_source_bucket(bucket_3)
    infected_topic = sns.Topic(self, "rInfectedTopic")
    if sc.infected_rule != None:
      sc.infected_rule.add_target(
        events_targets.SnsTopic(
          infected_topic,
          message=events.RuleTargetInput.from_event_path('$.detail.responsePayload.message'),
        )
      )
```

</p>
</details>

### Example 2. (Bring your own destinations)

<details><summary>typescript</summary>
<p>

```python
import {
  SqsDestination,
  EventBridgeDestination,
} from 'aws-cdk-lib/aws-lambda-destinations';
import { Bucket } from 'aws-cdk-lib/aws-s3';
import { Queue } from 'aws-cdk-lib/aws-sqs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { ServerlessClamscan } from 'cdk-serverless-clamscan';

export class CdkTestStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const bucket_1 = new Bucket(this, 'rBucket1');
    const bucket_2 = new Bucket(this, 'rBucket2');
    const bucketList = [bucket_1, bucket_2];
    const queue = new Queue(this, 'rQueue');
    const sc = new ServerlessClamscan(this, 'default', {
      buckets: bucketList,
      onResult: new EventBridgeDestination(),
      onError: new SqsDestination(queue),
    });
    const bucket_3 = new Bucket(this, 'rBucket3');
    sc.addSourceBucket(bucket_3);
  }
}
```

</p>
</details><details><summary>python</summary>
<p>

```python
from aws_cdk import (
  Stack,
  aws_lambda_destinations as lambda_destinations,
  aws_s3 as s3,
  aws_sqs as sqs
)
from cdk_serverless_clamscan import ServerlessClamscan
from constructs import Construct

class CdkTestStack(Stack):

  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    bucket_1 = s3.Bucket(self, "rBucket1")
    bucket_2 = s3.Bucket(self, "rBucket2")
    bucketList = [ bucket_1, bucket_2 ]
    queue = sqs.Queue(self, "rQueue")
    sc = ServerlessClamscan(self, "rClamScan",
      buckets=bucketList,
      on_result=lambda_destinations.EventBridgeDestination(),
      on_error=lambda_destinations.SqsDestination(queue),
    )
    bucket_3 = s3.Bucket(self, "rBucket3")
    sc.add_source_bucket(bucket_3)
```

</p>
</details>

## Operation and Maintenance

When ClamAV publishes updates to the scanner you will see “Your ClamAV installation is OUTDATED” in your scan results. While the construct creates a system to keep the database definitions up to date, you must update the scanner to detect all the latest Viruses.

Update the docker images of the Lambda functions with the latest version of ClamAV by re-running `cdk deploy`.

## API Reference

See [API.md](./API.md).

## Contributing

See [CONTRIBUTING](./CONTRIBUTING.md) for more information.

## License

This project is licensed under the Apache-2.0 License.
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

import aws_cdk.aws_efs
import aws_cdk.aws_events
import aws_cdk.aws_iam
import aws_cdk.aws_lambda
import aws_cdk.aws_s3
import aws_cdk.aws_sqs
import constructs


class ServerlessClamscan(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-serverless-clamscan.ServerlessClamscan",
):
    '''An `aws-cdk <https://github.com/aws/aws-cdk>`_ construct that uses `ClamAV® <https://www.clamav.net/>`_. to scan objects in Amazon S3 for viruses. The construct provides a flexible interface for a system to act based on the results of a ClamAV virus scan.

    The construct creates a Lambda function with EFS integration to support larger files.
    A VPC with isolated subnets, a S3 Gateway endpoint will also be created.

    Additionally creates an twice-daily job to download the latest ClamAV definition files to the
    Virus Definitions S3 Bucket by utilizing an EventBridge rule and a Lambda function and
    publishes CloudWatch Metrics to the 'serverless-clamscan' namespace.

    **Important O&M**:
    When ClamAV publishes updates to the scanner you will see “Your ClamAV installation is OUTDATED” in your scan results.
    While the construct creates a system to keep the database definitions up to date, you must update the scanner to
    detect all the latest Viruses.

    Update the docker images of the Lambda functions with the latest version of ClamAV by re-running ``cdk deploy``.

    Successful Scan Event format Example::

       {
           "source": "serverless-clamscan",
           "input_bucket": <input_bucket_name>,
           "input_key": <object_key>,
           "status": <"CLEAN"|"INFECTED"|"N/A">,
           "message": <scan_summary>,
         }

    Note: The Virus Definitions bucket policy will likely cause a deletion error if you choose to delete
    the stack associated in the construct. However since the bucket itself gets deleted, you can delete
    the stack again to resolve the error.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        accept_responsibility_for_using_imported_bucket: typing.Optional[builtins.bool] = None,
        buckets: typing.Optional[typing.Sequence[aws_cdk.aws_s3.IBucket]] = None,
        defs_bucket_access_logs_config: typing.Optional[typing.Union["ServerlessClamscanLoggingProps", typing.Dict[str, typing.Any]]] = None,
        efs_encryption: typing.Optional[builtins.bool] = None,
        efs_performance_mode: typing.Optional[aws_cdk.aws_efs.PerformanceMode] = None,
        on_error: typing.Optional[aws_cdk.aws_lambda.IDestination] = None,
        on_result: typing.Optional[aws_cdk.aws_lambda.IDestination] = None,
        reserved_concurrency: typing.Optional[jsii.Number] = None,
        scan_function_memory_size: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Creates a ServerlessClamscan construct.

        :param scope: The parent creating construct (usually ``this``).
        :param id: The construct's name.
        :param accept_responsibility_for_using_imported_bucket: Allows the use of imported buckets. When using imported buckets the user is responsible for adding the required policy statement to the bucket policy: ``getPolicyStatementForBucket()`` can be used to retrieve the policy statement required by the solution.
        :param buckets: An optional list of S3 buckets to configure for ClamAV Virus Scanning; buckets can be added later by calling addSourceBucket.
        :param defs_bucket_access_logs_config: Whether or not to enable Access Logging for the Virus Definitions bucket, you can specify an existing bucket and prefix (Default: Creates a new S3 Bucket for access logs).
        :param efs_encryption: Whether or not to enable encryption on EFS filesystem (Default: enabled).
        :param efs_performance_mode: Set the performance mode of the EFS file system (Default: GENERAL_PURPOSE).
        :param on_error: The Lambda Destination for files that fail to scan and are marked 'ERROR' or stuck 'IN PROGRESS' due to a Lambda timeout (Default: Creates and publishes to a new SQS queue if unspecified).
        :param on_result: The Lambda Destination for files marked 'CLEAN' or 'INFECTED' based on the ClamAV Virus scan or 'N/A' for scans triggered by S3 folder creation events marked (Default: Creates and publishes to a new Event Bridge Bus if unspecified).
        :param reserved_concurrency: Optionally set a reserved concurrency for the virus scanning Lambda.
        :param scan_function_memory_size: Optionally set the memory allocation for the scan function. Note that low memory allocations may cause errors. (Default: 10240).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServerlessClamscan.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ServerlessClamscanProps(
            accept_responsibility_for_using_imported_bucket=accept_responsibility_for_using_imported_bucket,
            buckets=buckets,
            defs_bucket_access_logs_config=defs_bucket_access_logs_config,
            efs_encryption=efs_encryption,
            efs_performance_mode=efs_performance_mode,
            on_error=on_error,
            on_result=on_result,
            reserved_concurrency=reserved_concurrency,
            scan_function_memory_size=scan_function_memory_size,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addSourceBucket")
    def add_source_bucket(self, bucket: aws_cdk.aws_s3.IBucket) -> None:
        '''Sets the specified S3 Bucket as a s3:ObjectCreate* for the ClamAV function.

        Grants the ClamAV function permissions to get and tag objects.
        Adds a bucket policy to disallow GetObject operations on files that are tagged 'IN PROGRESS', 'INFECTED', or 'ERROR'.

        :param bucket: The bucket to add the scanning bucket policy and s3:ObjectCreate* trigger to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServerlessClamscan.add_source_bucket)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
        return typing.cast(None, jsii.invoke(self, "addSourceBucket", [bucket]))

    @jsii.member(jsii_name="getPolicyStatementForBucket")
    def get_policy_statement_for_bucket(
        self,
        bucket: aws_cdk.aws_s3.IBucket,
    ) -> aws_cdk.aws_iam.PolicyStatement:
        '''Returns the statement that should be added to the bucket policy in order to prevent objects to be accessed when they are not clean or there have been scanning errors: this policy should be added manually if external buckets are passed to addSourceBucket().

        :param bucket: The bucket which you need to protect with the policy.

        :return: PolicyStatement the policy statement if available
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServerlessClamscan.get_policy_statement_for_bucket)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
        return typing.cast(aws_cdk.aws_iam.PolicyStatement, jsii.invoke(self, "getPolicyStatementForBucket", [bucket]))

    @builtins.property
    @jsii.member(jsii_name="errorDest")
    def error_dest(self) -> aws_cdk.aws_lambda.IDestination:
        '''The Lambda Destination for failed on erred scans [ERROR, IN PROGRESS (If error is due to Lambda timeout)].'''
        return typing.cast(aws_cdk.aws_lambda.IDestination, jsii.get(self, "errorDest"))

    @builtins.property
    @jsii.member(jsii_name="resultDest")
    def result_dest(self) -> aws_cdk.aws_lambda.IDestination:
        '''The Lambda Destination for completed ClamAV scans [CLEAN, INFECTED].'''
        return typing.cast(aws_cdk.aws_lambda.IDestination, jsii.get(self, "resultDest"))

    @builtins.property
    @jsii.member(jsii_name="scanAssumedPrincipal")
    def scan_assumed_principal(self) -> aws_cdk.aws_iam.ArnPrincipal:
        '''
        :return: ArnPrincipal the ARN of the assumed role principal for the scan function
        '''
        return typing.cast(aws_cdk.aws_iam.ArnPrincipal, jsii.get(self, "scanAssumedPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="cleanRule")
    def clean_rule(self) -> typing.Optional[aws_cdk.aws_events.Rule]:
        '''Conditional: An Event Bridge Rule for files that are marked 'CLEAN' by ClamAV if a success destination was not specified.'''
        return typing.cast(typing.Optional[aws_cdk.aws_events.Rule], jsii.get(self, "cleanRule"))

    @builtins.property
    @jsii.member(jsii_name="defsAccessLogsBucket")
    def defs_access_logs_bucket(self) -> typing.Optional[aws_cdk.aws_s3.IBucket]:
        '''Conditional: The Bucket for access logs for the virus definitions bucket if logging is enabled (defsBucketAccessLogsConfig).'''
        return typing.cast(typing.Optional[aws_cdk.aws_s3.IBucket], jsii.get(self, "defsAccessLogsBucket"))

    @builtins.property
    @jsii.member(jsii_name="errorDeadLetterQueue")
    def error_dead_letter_queue(self) -> typing.Optional[aws_cdk.aws_sqs.Queue]:
        '''Conditional: The SQS Dead Letter Queue for the errorQueue if a failure (onError) destination was not specified.'''
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.Queue], jsii.get(self, "errorDeadLetterQueue"))

    @builtins.property
    @jsii.member(jsii_name="errorQueue")
    def error_queue(self) -> typing.Optional[aws_cdk.aws_sqs.Queue]:
        '''Conditional: The SQS Queue for erred scans if a failure (onError) destination was not specified.'''
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.Queue], jsii.get(self, "errorQueue"))

    @builtins.property
    @jsii.member(jsii_name="infectedRule")
    def infected_rule(self) -> typing.Optional[aws_cdk.aws_events.Rule]:
        '''Conditional: An Event Bridge Rule for files that are marked 'INFECTED' by ClamAV if a success destination was not specified.'''
        return typing.cast(typing.Optional[aws_cdk.aws_events.Rule], jsii.get(self, "infectedRule"))

    @builtins.property
    @jsii.member(jsii_name="resultBus")
    def result_bus(self) -> typing.Optional[aws_cdk.aws_events.EventBus]:
        '''Conditional: The Event Bridge Bus for completed ClamAV scans if a success (onResult) destination was not specified.'''
        return typing.cast(typing.Optional[aws_cdk.aws_events.EventBus], jsii.get(self, "resultBus"))

    @builtins.property
    @jsii.member(jsii_name="useImportedBuckets")
    def use_imported_buckets(self) -> typing.Optional[builtins.bool]:
        '''Conditional: When true, the user accepted the responsibility for using imported buckets.'''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "useImportedBuckets"))


@jsii.data_type(
    jsii_type="cdk-serverless-clamscan.ServerlessClamscanLoggingProps",
    jsii_struct_bases=[],
    name_mapping={"logs_bucket": "logsBucket", "logs_prefix": "logsPrefix"},
)
class ServerlessClamscanLoggingProps:
    def __init__(
        self,
        *,
        logs_bucket: typing.Optional[typing.Union[builtins.bool, aws_cdk.aws_s3.IBucket]] = None,
        logs_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Interface for ServerlessClamscan Virus Definitions S3 Bucket Logging.

        :param logs_bucket: Destination bucket for the server access logs (Default: Creates a new S3 Bucket for access logs).
        :param logs_prefix: Optional log file prefix to use for the bucket's access logs, option is ignored if logs_bucket is set to false.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServerlessClamscanLoggingProps.__init__)
            check_type(argname="argument logs_bucket", value=logs_bucket, expected_type=type_hints["logs_bucket"])
            check_type(argname="argument logs_prefix", value=logs_prefix, expected_type=type_hints["logs_prefix"])
        self._values: typing.Dict[str, typing.Any] = {}
        if logs_bucket is not None:
            self._values["logs_bucket"] = logs_bucket
        if logs_prefix is not None:
            self._values["logs_prefix"] = logs_prefix

    @builtins.property
    def logs_bucket(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.aws_s3.IBucket]]:
        '''Destination bucket for the server access logs (Default: Creates a new S3 Bucket for access logs).'''
        result = self._values.get("logs_bucket")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.aws_s3.IBucket]], result)

    @builtins.property
    def logs_prefix(self) -> typing.Optional[builtins.str]:
        '''Optional log file prefix to use for the bucket's access logs, option is ignored if logs_bucket is set to false.'''
        result = self._values.get("logs_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerlessClamscanLoggingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-serverless-clamscan.ServerlessClamscanProps",
    jsii_struct_bases=[],
    name_mapping={
        "accept_responsibility_for_using_imported_bucket": "acceptResponsibilityForUsingImportedBucket",
        "buckets": "buckets",
        "defs_bucket_access_logs_config": "defsBucketAccessLogsConfig",
        "efs_encryption": "efsEncryption",
        "efs_performance_mode": "efsPerformanceMode",
        "on_error": "onError",
        "on_result": "onResult",
        "reserved_concurrency": "reservedConcurrency",
        "scan_function_memory_size": "scanFunctionMemorySize",
    },
)
class ServerlessClamscanProps:
    def __init__(
        self,
        *,
        accept_responsibility_for_using_imported_bucket: typing.Optional[builtins.bool] = None,
        buckets: typing.Optional[typing.Sequence[aws_cdk.aws_s3.IBucket]] = None,
        defs_bucket_access_logs_config: typing.Optional[typing.Union[ServerlessClamscanLoggingProps, typing.Dict[str, typing.Any]]] = None,
        efs_encryption: typing.Optional[builtins.bool] = None,
        efs_performance_mode: typing.Optional[aws_cdk.aws_efs.PerformanceMode] = None,
        on_error: typing.Optional[aws_cdk.aws_lambda.IDestination] = None,
        on_result: typing.Optional[aws_cdk.aws_lambda.IDestination] = None,
        reserved_concurrency: typing.Optional[jsii.Number] = None,
        scan_function_memory_size: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Interface for creating a ServerlessClamscan.

        :param accept_responsibility_for_using_imported_bucket: Allows the use of imported buckets. When using imported buckets the user is responsible for adding the required policy statement to the bucket policy: ``getPolicyStatementForBucket()`` can be used to retrieve the policy statement required by the solution.
        :param buckets: An optional list of S3 buckets to configure for ClamAV Virus Scanning; buckets can be added later by calling addSourceBucket.
        :param defs_bucket_access_logs_config: Whether or not to enable Access Logging for the Virus Definitions bucket, you can specify an existing bucket and prefix (Default: Creates a new S3 Bucket for access logs).
        :param efs_encryption: Whether or not to enable encryption on EFS filesystem (Default: enabled).
        :param efs_performance_mode: Set the performance mode of the EFS file system (Default: GENERAL_PURPOSE).
        :param on_error: The Lambda Destination for files that fail to scan and are marked 'ERROR' or stuck 'IN PROGRESS' due to a Lambda timeout (Default: Creates and publishes to a new SQS queue if unspecified).
        :param on_result: The Lambda Destination for files marked 'CLEAN' or 'INFECTED' based on the ClamAV Virus scan or 'N/A' for scans triggered by S3 folder creation events marked (Default: Creates and publishes to a new Event Bridge Bus if unspecified).
        :param reserved_concurrency: Optionally set a reserved concurrency for the virus scanning Lambda.
        :param scan_function_memory_size: Optionally set the memory allocation for the scan function. Note that low memory allocations may cause errors. (Default: 10240).
        '''
        if isinstance(defs_bucket_access_logs_config, dict):
            defs_bucket_access_logs_config = ServerlessClamscanLoggingProps(**defs_bucket_access_logs_config)
        if __debug__:
            type_hints = typing.get_type_hints(ServerlessClamscanProps.__init__)
            check_type(argname="argument accept_responsibility_for_using_imported_bucket", value=accept_responsibility_for_using_imported_bucket, expected_type=type_hints["accept_responsibility_for_using_imported_bucket"])
            check_type(argname="argument buckets", value=buckets, expected_type=type_hints["buckets"])
            check_type(argname="argument defs_bucket_access_logs_config", value=defs_bucket_access_logs_config, expected_type=type_hints["defs_bucket_access_logs_config"])
            check_type(argname="argument efs_encryption", value=efs_encryption, expected_type=type_hints["efs_encryption"])
            check_type(argname="argument efs_performance_mode", value=efs_performance_mode, expected_type=type_hints["efs_performance_mode"])
            check_type(argname="argument on_error", value=on_error, expected_type=type_hints["on_error"])
            check_type(argname="argument on_result", value=on_result, expected_type=type_hints["on_result"])
            check_type(argname="argument reserved_concurrency", value=reserved_concurrency, expected_type=type_hints["reserved_concurrency"])
            check_type(argname="argument scan_function_memory_size", value=scan_function_memory_size, expected_type=type_hints["scan_function_memory_size"])
        self._values: typing.Dict[str, typing.Any] = {}
        if accept_responsibility_for_using_imported_bucket is not None:
            self._values["accept_responsibility_for_using_imported_bucket"] = accept_responsibility_for_using_imported_bucket
        if buckets is not None:
            self._values["buckets"] = buckets
        if defs_bucket_access_logs_config is not None:
            self._values["defs_bucket_access_logs_config"] = defs_bucket_access_logs_config
        if efs_encryption is not None:
            self._values["efs_encryption"] = efs_encryption
        if efs_performance_mode is not None:
            self._values["efs_performance_mode"] = efs_performance_mode
        if on_error is not None:
            self._values["on_error"] = on_error
        if on_result is not None:
            self._values["on_result"] = on_result
        if reserved_concurrency is not None:
            self._values["reserved_concurrency"] = reserved_concurrency
        if scan_function_memory_size is not None:
            self._values["scan_function_memory_size"] = scan_function_memory_size

    @builtins.property
    def accept_responsibility_for_using_imported_bucket(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Allows the use of imported buckets.

        When using imported buckets the user is responsible for adding the required policy statement to the bucket policy: ``getPolicyStatementForBucket()`` can be used to retrieve the policy statement required by the solution.
        '''
        result = self._values.get("accept_responsibility_for_using_imported_bucket")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def buckets(self) -> typing.Optional[typing.List[aws_cdk.aws_s3.IBucket]]:
        '''An optional list of S3 buckets to configure for ClamAV Virus Scanning;

        buckets can be added later by calling addSourceBucket.
        '''
        result = self._values.get("buckets")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_s3.IBucket]], result)

    @builtins.property
    def defs_bucket_access_logs_config(
        self,
    ) -> typing.Optional[ServerlessClamscanLoggingProps]:
        '''Whether or not to enable Access Logging for the Virus Definitions bucket, you can specify an existing bucket and prefix (Default: Creates a new S3 Bucket for access logs).'''
        result = self._values.get("defs_bucket_access_logs_config")
        return typing.cast(typing.Optional[ServerlessClamscanLoggingProps], result)

    @builtins.property
    def efs_encryption(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to enable encryption on EFS filesystem (Default: enabled).'''
        result = self._values.get("efs_encryption")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def efs_performance_mode(self) -> typing.Optional[aws_cdk.aws_efs.PerformanceMode]:
        '''Set the performance mode of the EFS file system (Default: GENERAL_PURPOSE).'''
        result = self._values.get("efs_performance_mode")
        return typing.cast(typing.Optional[aws_cdk.aws_efs.PerformanceMode], result)

    @builtins.property
    def on_error(self) -> typing.Optional[aws_cdk.aws_lambda.IDestination]:
        '''The Lambda Destination for files that fail to scan and are marked 'ERROR' or stuck 'IN PROGRESS' due to a Lambda timeout (Default: Creates and publishes to a new SQS queue if unspecified).'''
        result = self._values.get("on_error")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.IDestination], result)

    @builtins.property
    def on_result(self) -> typing.Optional[aws_cdk.aws_lambda.IDestination]:
        '''The Lambda Destination for files marked 'CLEAN' or 'INFECTED' based on the ClamAV Virus scan or 'N/A' for scans triggered by S3 folder creation events marked (Default: Creates and publishes to a new Event Bridge Bus if unspecified).'''
        result = self._values.get("on_result")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.IDestination], result)

    @builtins.property
    def reserved_concurrency(self) -> typing.Optional[jsii.Number]:
        '''Optionally set a reserved concurrency for the virus scanning Lambda.

        :see: https://docs.aws.amazon.com/lambda/latest/operatorguide/reserved-concurrency.html
        '''
        result = self._values.get("reserved_concurrency")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scan_function_memory_size(self) -> typing.Optional[jsii.Number]:
        '''Optionally set the memory allocation for the scan function.

        Note that low memory allocations may cause errors. (Default: 10240).

        :see: https://docs.aws.amazon.com/lambda/latest/operatorguide/computing-power.html
        '''
        result = self._values.get("scan_function_memory_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerlessClamscanProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ServerlessClamscan",
    "ServerlessClamscanLoggingProps",
    "ServerlessClamscanProps",
]

publication.publish()
