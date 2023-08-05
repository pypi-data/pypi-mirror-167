'''
[![NPM version](https://badge.fury.io/js/low-cost-ecs.svg)](https://www.npmjs.com/package/low-cost-ecs)
[![PyPI version](https://badge.fury.io/py/low-cost-ecs.svg)](https://pypi.org/project/low-cost-ecs)
[![Release](https://github.com/rajyan/low-cost-ecs/workflows/release/badge.svg)](https://github.com/rajyan/low-cost-ecs/actions/workflows/release.yml)
[<img src="https://constructs.dev/badge?package=low-cost-ecs" width="150">](https://constructs.dev/packages/low-cost-ecs)

# Low-Cost ECS

A CDK construct that provides easy and [low-cost](#cost) ECS on EC2 server setup without a load balancer.

**This construct is for development purposes only**. See [Limitations](#limitations).

# Try it out!

The easiest way to see what this construct creates is to clone this repository and deploy the sample server.
Edit settings in `bin/low-cost-ecs.ts` and deploy the cdk construct. [Public hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/AboutHZWorkingWith.html) is required.

```
git clone https://github.com/rajyan/low-cost-ecs.git
# edit settings in bin/low-cost-ecs.ts
npx cdk deploy
```

Access to configured `recordDomainNames` and see that the nginx sample server has been deployed.

# Installation

To use this construct in your cdk stack as a library,

```
npm install low-cost-ecs
```

```python
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { LowCostECS } from 'low-cost-ecs';

class SampleStack extends Stack {
    constructor(scope: Construct, id: string, props?: StackProps) {
        super(scope, id, props);

        const vpc = { /** Your VPC */ };
        const securityGroup = {/** Your security group */ };
        const serverTaskDefinition = {/** Your task definition */ };

        new LowCostECS(this, 'LowCostECS', {
            hostedZoneDomain: "rajyan.net",
            email: "kitakita7617@gmail.com",
            vpc: vpc,
            securityGroup: securityGroup,
            serverTaskDefinition: serverTaskDefinition
        });
    }
}
```

The required fields are `hostedZoneDomain` and `email`.
You can configure your server task definition and other props. Read [`LowCostECSProps` documentation](https://github.com/rajyan/low-cost-ecs/blob/main/API.md#low-cost-ecs.LowCostECSProps) for details.

# Why

ECS may often seem expensive when used for personal development purposes, because of the cost of the load balancer.
The application load balancer is a great service because it is easy to set up managed ACM certificates, it scales, and has dynamic port mappings and so on,
but it is over-featured for running 1 ECS service.

However, to run an ECS server without a load balancer, you need to associate an Elastic IP to the host instance and install your certificate by yourself.
This construct aims to automate these works and to make it easy to deploy resources to run a low-cost ECS server.

# Overview

Resources generated in this stack

* Route53 A record

  * Forwarding to host instance Elastic IP
* Certificate State Machine

  * Install and renew certificates to EFS using [certbot-dns-route53](https://certbot-dns-route53.readthedocs.io/en/stable/)
  * Scheduled automated renewal every 60 days
  * Email notification on certbot task failure
* ECS on EC2 host instance

  * ECS-optimized Amazon Linux 2 AMI instance auto-scaling group
  * Automatically associated with Elastic IP on instance initialization
* ECS Service

  * TLS/SSL certificate installation on default container startup
  * Certificate EFS mounted on `/etc/letsencrypt`
* Others

  * VPC with only public subnets (no NAT Gateways to decrease cost)
  * Security groups with minimum inbounds
  * IAM roles with minimum privileges

# Cost

All resources except Route53 HostedZone should be included in [AWS Free Tier](https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/get-started-with-the-aws-free-tier.html)
***if you are in the 12 Months Free period***.
After your 12 Months Free period, setting [`hostInstanceSpotPrice`](https://github.com/rajyan/low-cost-ecs/blob/main/API.md#low-cost-ecs.LowCostECSProps.property.hostInstanceSpotPrice) to use spot instances is recommended.

* EC2

  * t2.micro 750 instance hours (12 Months Free Tier)
  * 30GB EBS volume (12 Months Free Tier)
* ECS

  * No additional charge because using ECS on EC2
* EFS

  * Usage is very small, it should be free
* Cloud Watch

  * Usage is very small, and it should be included in the free tier
  * Enabling [`containerInsights`](https://github.com/rajyan/low-cost-ecs/blob/main/API.md#low-cost-ecs.LowCostECSProps.property.containerInsights) will charge for custom metrics

# Debugging

* SSM Session Manager

SSM manager is pre-installed (in ECS-optimized Amazon Linux 2 AMI) in the host instance and `AmazonSSMManagedInstanceCore` is added to the host instance role
to access and debug in your host instance.

```
aws ssm start-session --target $INSTANCE_ID
```

* ECS Exec

Service ECS Exec is enabled, so execute commands can be used to debug in your server task container.

```
aws ecs execute-command \
--cluster $CLUSTER_ID \
--task $TASK_ID \
--container nginx \
--command bash \
--interactive
```

# Limitations

The ECS service occupies the host port, only one service can be run at a time.
The old task must be terminated before the new task launches, and this causes downtime on release.

Also, if you make changes that require recreating service, you may need to manually terminate the task of old the service.
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

import aws_cdk
import aws_cdk.aws_ec2
import aws_cdk.aws_ecs
import aws_cdk.aws_logs
import constructs


class LowCostECS(
    aws_cdk.Stack,
    metaclass=jsii.JSIIMeta,
    jsii_type="low-cost-ecs.LowCostECS",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        email: builtins.str,
        hosted_zone_domain: builtins.str,
        aws_cli_docker_tag: typing.Optional[builtins.str] = None,
        certbot_docker_tag: typing.Optional[builtins.str] = None,
        certbot_schedule_interval: typing.Optional[jsii.Number] = None,
        container_insights: typing.Optional[builtins.bool] = None,
        host_instance_spot_price: typing.Optional[builtins.str] = None,
        host_instance_type: typing.Optional[builtins.str] = None,
        log_group: typing.Optional[aws_cdk.aws_logs.ILogGroup] = None,
        record_domain_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.SecurityGroup] = None,
        server_task_definition: typing.Optional[aws_cdk.aws_ecs.Ec2TaskDefinition] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        analytics_reporting: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        env: typing.Optional[typing.Union[aws_cdk.Environment, typing.Dict[str, typing.Any]]] = None,
        stack_name: typing.Optional[builtins.str] = None,
        synthesizer: typing.Optional[aws_cdk.IStackSynthesizer] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        termination_protection: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param email: (experimental) Email for expiration emails to register to your let's encrypt account.
        :param hosted_zone_domain: (experimental) Domain name of the hosted zone.
        :param aws_cli_docker_tag: (experimental) Docker image tag of amazon/aws-cli. This image is used to associate elastic ip on host instance startup, and run certbot cfn on ecs container startup. Default: - latest
        :param certbot_docker_tag: (experimental) Docker image tag of certbot/dns-route53 to create certificates. Default: - v1.29.0
        :param certbot_schedule_interval: (experimental) Certbot task schedule interval in days to renew the certificate. Default: - 60
        :param container_insights: (experimental) Enable container insights or not. Default: - undefined (container insights disabled)
        :param host_instance_spot_price: (experimental) The maximum hourly price (in USD) to be paid for any Spot Instance launched to fulfill the request. Host instance asg would use spot instances if hostInstanceSpotPrice is set. Default: - undefined
        :param host_instance_type: (experimental) Instance type of the ECS host instance. Default: - t2.micro
        :param log_group: (experimental) Log group of the certbot task and the aws-cli task. Default: - Creates default cdk log group
        :param record_domain_names: (experimental) Domain names for A records to elastic ip of ECS host instance. Default: - [ props.hostedZone.zoneName ]
        :param removal_policy: (experimental) Removal policy for the file system and log group (if using default). Default: - RemovalPolicy.DESTROY
        :param security_group: (experimental) Security group of the ECS host instance. Default: - Creates security group with allowAllOutbound and ingress rule (ipv4, ipv6) => (tcp 80, 443).
        :param server_task_definition: (experimental) Task definition for the server ecs task. Default: - Nginx server task definition defined in sampleServerTask()
        :param vpc: (experimental) Vpc of the ECS host instance and cluster. Default: - Creates vpc with only public subnets and no NAT gateways.
        :param analytics_reporting: Include runtime versioning information in this Stack. Default: ``analyticsReporting`` setting of containing ``App``, or value of 'aws:cdk:version-reporting' context key
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Set the ``region``/``account`` fields of ``env`` to either a concrete value to select the indicated environment (recommended for production stacks), or to the values of environment variables ``CDK_DEFAULT_REGION``/``CDK_DEFAULT_ACCOUNT`` to let the target environment depend on the AWS credentials/configuration that the CDK CLI is executed under (recommended for development stacks). If the ``Stack`` is instantiated inside a ``Stage``, any undefined ``region``/``account`` fields from ``env`` will default to the same field on the encompassing ``Stage``, if configured there. If either ``region`` or ``account`` are not set nor inherited from ``Stage``, the Stack will be considered "*environment-agnostic*"". Environment-agnostic stacks can be deployed to any environment but may not be able to take advantage of all features of the CDK. For example, they will not be able to use environmental context lookups such as ``ec2.Vpc.fromLookup`` and will not automatically translate Service Principals to the right format based on the environment's AWS partition, and other such enhancements. Default: - The environment of the containing ``Stage`` if available, otherwise create the stack will be environment-agnostic.
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param synthesizer: Synthesis method to use while deploying this stack. Default: - ``DefaultStackSynthesizer`` if the ``@aws-cdk/core:newStyleStackSynthesis`` feature flag is set, ``LegacyStackSynthesizer`` otherwise.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        :param termination_protection: Whether to enable termination protection for this stack. Default: false

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LowCostECS.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = LowCostECSProps(
            email=email,
            hosted_zone_domain=hosted_zone_domain,
            aws_cli_docker_tag=aws_cli_docker_tag,
            certbot_docker_tag=certbot_docker_tag,
            certbot_schedule_interval=certbot_schedule_interval,
            container_insights=container_insights,
            host_instance_spot_price=host_instance_spot_price,
            host_instance_type=host_instance_type,
            log_group=log_group,
            record_domain_names=record_domain_names,
            removal_policy=removal_policy,
            security_group=security_group,
            server_task_definition=server_task_definition,
            vpc=vpc,
            analytics_reporting=analytics_reporting,
            description=description,
            env=env,
            stack_name=stack_name,
            synthesizer=synthesizer,
            tags=tags,
            termination_protection=termination_protection,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="low-cost-ecs.LowCostECSProps",
    jsii_struct_bases=[aws_cdk.StackProps],
    name_mapping={
        "analytics_reporting": "analyticsReporting",
        "description": "description",
        "env": "env",
        "stack_name": "stackName",
        "synthesizer": "synthesizer",
        "tags": "tags",
        "termination_protection": "terminationProtection",
        "email": "email",
        "hosted_zone_domain": "hostedZoneDomain",
        "aws_cli_docker_tag": "awsCliDockerTag",
        "certbot_docker_tag": "certbotDockerTag",
        "certbot_schedule_interval": "certbotScheduleInterval",
        "container_insights": "containerInsights",
        "host_instance_spot_price": "hostInstanceSpotPrice",
        "host_instance_type": "hostInstanceType",
        "log_group": "logGroup",
        "record_domain_names": "recordDomainNames",
        "removal_policy": "removalPolicy",
        "security_group": "securityGroup",
        "server_task_definition": "serverTaskDefinition",
        "vpc": "vpc",
    },
)
class LowCostECSProps(aws_cdk.StackProps):
    def __init__(
        self,
        *,
        analytics_reporting: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        env: typing.Optional[typing.Union[aws_cdk.Environment, typing.Dict[str, typing.Any]]] = None,
        stack_name: typing.Optional[builtins.str] = None,
        synthesizer: typing.Optional[aws_cdk.IStackSynthesizer] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        termination_protection: typing.Optional[builtins.bool] = None,
        email: builtins.str,
        hosted_zone_domain: builtins.str,
        aws_cli_docker_tag: typing.Optional[builtins.str] = None,
        certbot_docker_tag: typing.Optional[builtins.str] = None,
        certbot_schedule_interval: typing.Optional[jsii.Number] = None,
        container_insights: typing.Optional[builtins.bool] = None,
        host_instance_spot_price: typing.Optional[builtins.str] = None,
        host_instance_type: typing.Optional[builtins.str] = None,
        log_group: typing.Optional[aws_cdk.aws_logs.ILogGroup] = None,
        record_domain_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.SecurityGroup] = None,
        server_task_definition: typing.Optional[aws_cdk.aws_ecs.Ec2TaskDefinition] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
    ) -> None:
        '''
        :param analytics_reporting: Include runtime versioning information in this Stack. Default: ``analyticsReporting`` setting of containing ``App``, or value of 'aws:cdk:version-reporting' context key
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Set the ``region``/``account`` fields of ``env`` to either a concrete value to select the indicated environment (recommended for production stacks), or to the values of environment variables ``CDK_DEFAULT_REGION``/``CDK_DEFAULT_ACCOUNT`` to let the target environment depend on the AWS credentials/configuration that the CDK CLI is executed under (recommended for development stacks). If the ``Stack`` is instantiated inside a ``Stage``, any undefined ``region``/``account`` fields from ``env`` will default to the same field on the encompassing ``Stage``, if configured there. If either ``region`` or ``account`` are not set nor inherited from ``Stage``, the Stack will be considered "*environment-agnostic*"". Environment-agnostic stacks can be deployed to any environment but may not be able to take advantage of all features of the CDK. For example, they will not be able to use environmental context lookups such as ``ec2.Vpc.fromLookup`` and will not automatically translate Service Principals to the right format based on the environment's AWS partition, and other such enhancements. Default: - The environment of the containing ``Stage`` if available, otherwise create the stack will be environment-agnostic.
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param synthesizer: Synthesis method to use while deploying this stack. Default: - ``DefaultStackSynthesizer`` if the ``@aws-cdk/core:newStyleStackSynthesis`` feature flag is set, ``LegacyStackSynthesizer`` otherwise.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        :param termination_protection: Whether to enable termination protection for this stack. Default: false
        :param email: (experimental) Email for expiration emails to register to your let's encrypt account.
        :param hosted_zone_domain: (experimental) Domain name of the hosted zone.
        :param aws_cli_docker_tag: (experimental) Docker image tag of amazon/aws-cli. This image is used to associate elastic ip on host instance startup, and run certbot cfn on ecs container startup. Default: - latest
        :param certbot_docker_tag: (experimental) Docker image tag of certbot/dns-route53 to create certificates. Default: - v1.29.0
        :param certbot_schedule_interval: (experimental) Certbot task schedule interval in days to renew the certificate. Default: - 60
        :param container_insights: (experimental) Enable container insights or not. Default: - undefined (container insights disabled)
        :param host_instance_spot_price: (experimental) The maximum hourly price (in USD) to be paid for any Spot Instance launched to fulfill the request. Host instance asg would use spot instances if hostInstanceSpotPrice is set. Default: - undefined
        :param host_instance_type: (experimental) Instance type of the ECS host instance. Default: - t2.micro
        :param log_group: (experimental) Log group of the certbot task and the aws-cli task. Default: - Creates default cdk log group
        :param record_domain_names: (experimental) Domain names for A records to elastic ip of ECS host instance. Default: - [ props.hostedZone.zoneName ]
        :param removal_policy: (experimental) Removal policy for the file system and log group (if using default). Default: - RemovalPolicy.DESTROY
        :param security_group: (experimental) Security group of the ECS host instance. Default: - Creates security group with allowAllOutbound and ingress rule (ipv4, ipv6) => (tcp 80, 443).
        :param server_task_definition: (experimental) Task definition for the server ecs task. Default: - Nginx server task definition defined in sampleServerTask()
        :param vpc: (experimental) Vpc of the ECS host instance and cluster. Default: - Creates vpc with only public subnets and no NAT gateways.

        :stability: experimental
        '''
        if isinstance(env, dict):
            env = aws_cdk.Environment(**env)
        if __debug__:
            type_hints = typing.get_type_hints(LowCostECSProps.__init__)
            check_type(argname="argument analytics_reporting", value=analytics_reporting, expected_type=type_hints["analytics_reporting"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
            check_type(argname="argument stack_name", value=stack_name, expected_type=type_hints["stack_name"])
            check_type(argname="argument synthesizer", value=synthesizer, expected_type=type_hints["synthesizer"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument termination_protection", value=termination_protection, expected_type=type_hints["termination_protection"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument hosted_zone_domain", value=hosted_zone_domain, expected_type=type_hints["hosted_zone_domain"])
            check_type(argname="argument aws_cli_docker_tag", value=aws_cli_docker_tag, expected_type=type_hints["aws_cli_docker_tag"])
            check_type(argname="argument certbot_docker_tag", value=certbot_docker_tag, expected_type=type_hints["certbot_docker_tag"])
            check_type(argname="argument certbot_schedule_interval", value=certbot_schedule_interval, expected_type=type_hints["certbot_schedule_interval"])
            check_type(argname="argument container_insights", value=container_insights, expected_type=type_hints["container_insights"])
            check_type(argname="argument host_instance_spot_price", value=host_instance_spot_price, expected_type=type_hints["host_instance_spot_price"])
            check_type(argname="argument host_instance_type", value=host_instance_type, expected_type=type_hints["host_instance_type"])
            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
            check_type(argname="argument record_domain_names", value=record_domain_names, expected_type=type_hints["record_domain_names"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument server_task_definition", value=server_task_definition, expected_type=type_hints["server_task_definition"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[str, typing.Any] = {
            "email": email,
            "hosted_zone_domain": hosted_zone_domain,
        }
        if analytics_reporting is not None:
            self._values["analytics_reporting"] = analytics_reporting
        if description is not None:
            self._values["description"] = description
        if env is not None:
            self._values["env"] = env
        if stack_name is not None:
            self._values["stack_name"] = stack_name
        if synthesizer is not None:
            self._values["synthesizer"] = synthesizer
        if tags is not None:
            self._values["tags"] = tags
        if termination_protection is not None:
            self._values["termination_protection"] = termination_protection
        if aws_cli_docker_tag is not None:
            self._values["aws_cli_docker_tag"] = aws_cli_docker_tag
        if certbot_docker_tag is not None:
            self._values["certbot_docker_tag"] = certbot_docker_tag
        if certbot_schedule_interval is not None:
            self._values["certbot_schedule_interval"] = certbot_schedule_interval
        if container_insights is not None:
            self._values["container_insights"] = container_insights
        if host_instance_spot_price is not None:
            self._values["host_instance_spot_price"] = host_instance_spot_price
        if host_instance_type is not None:
            self._values["host_instance_type"] = host_instance_type
        if log_group is not None:
            self._values["log_group"] = log_group
        if record_domain_names is not None:
            self._values["record_domain_names"] = record_domain_names
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if security_group is not None:
            self._values["security_group"] = security_group
        if server_task_definition is not None:
            self._values["server_task_definition"] = server_task_definition
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def analytics_reporting(self) -> typing.Optional[builtins.bool]:
        '''Include runtime versioning information in this Stack.

        :default:

        ``analyticsReporting`` setting of containing ``App``, or value of
        'aws:cdk:version-reporting' context key
        '''
        result = self._values.get("analytics_reporting")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the stack.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def env(self) -> typing.Optional[aws_cdk.Environment]:
        '''The AWS environment (account/region) where this stack will be deployed.

        Set the ``region``/``account`` fields of ``env`` to either a concrete value to
        select the indicated environment (recommended for production stacks), or to
        the values of environment variables
        ``CDK_DEFAULT_REGION``/``CDK_DEFAULT_ACCOUNT`` to let the target environment
        depend on the AWS credentials/configuration that the CDK CLI is executed
        under (recommended for development stacks).

        If the ``Stack`` is instantiated inside a ``Stage``, any undefined
        ``region``/``account`` fields from ``env`` will default to the same field on the
        encompassing ``Stage``, if configured there.

        If either ``region`` or ``account`` are not set nor inherited from ``Stage``, the
        Stack will be considered "*environment-agnostic*"". Environment-agnostic
        stacks can be deployed to any environment but may not be able to take
        advantage of all features of the CDK. For example, they will not be able to
        use environmental context lookups such as ``ec2.Vpc.fromLookup`` and will not
        automatically translate Service Principals to the right format based on the
        environment's AWS partition, and other such enhancements.

        :default:

        - The environment of the containing ``Stage`` if available,
        otherwise create the stack will be environment-agnostic.

        Example::

            // Use a concrete account and region to deploy this stack to:
            // `.account` and `.region` will simply return these values.
            new Stack(app, 'Stack1', {
              env: {
                account: '123456789012',
                region: 'us-east-1'
              },
            });
            
            // Use the CLI's current credentials to determine the target environment:
            // `.account` and `.region` will reflect the account+region the CLI
            // is configured to use (based on the user CLI credentials)
            new Stack(app, 'Stack2', {
              env: {
                account: process.env.CDK_DEFAULT_ACCOUNT,
                region: process.env.CDK_DEFAULT_REGION
              },
            });
            
            // Define multiple stacks stage associated with an environment
            const myStage = new Stage(app, 'MyStage', {
              env: {
                account: '123456789012',
                region: 'us-east-1'
              }
            });
            
            // both of these stacks will use the stage's account/region:
            // `.account` and `.region` will resolve to the concrete values as above
            new MyStack(myStage, 'Stack1');
            new YourStack(myStage, 'Stack2');
            
            // Define an environment-agnostic stack:
            // `.account` and `.region` will resolve to `{ "Ref": "AWS::AccountId" }` and `{ "Ref": "AWS::Region" }` respectively.
            // which will only resolve to actual values by CloudFormation during deployment.
            new MyStack(app, 'Stack1');
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[aws_cdk.Environment], result)

    @builtins.property
    def stack_name(self) -> typing.Optional[builtins.str]:
        '''Name to deploy the stack with.

        :default: - Derived from construct path.
        '''
        result = self._values.get("stack_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def synthesizer(self) -> typing.Optional[aws_cdk.IStackSynthesizer]:
        '''Synthesis method to use while deploying this stack.

        :default:

        - ``DefaultStackSynthesizer`` if the ``@aws-cdk/core:newStyleStackSynthesis`` feature flag
        is set, ``LegacyStackSynthesizer`` otherwise.
        '''
        result = self._values.get("synthesizer")
        return typing.cast(typing.Optional[aws_cdk.IStackSynthesizer], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Stack tags that will be applied to all the taggable resources and the stack itself.

        :default: {}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def termination_protection(self) -> typing.Optional[builtins.bool]:
        '''Whether to enable termination protection for this stack.

        :default: false
        '''
        result = self._values.get("termination_protection")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def email(self) -> builtins.str:
        '''(experimental) Email for expiration emails to register to your let's encrypt account.

        :stability: experimental
        :link: https://docs.aws.amazon.com/sns/latest/dg/sns-email-notifications.html
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hosted_zone_domain(self) -> builtins.str:
        '''(experimental) Domain name of the hosted zone.

        :stability: experimental
        '''
        result = self._values.get("hosted_zone_domain")
        assert result is not None, "Required property 'hosted_zone_domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_cli_docker_tag(self) -> typing.Optional[builtins.str]:
        '''(experimental) Docker image tag of amazon/aws-cli.

        This image is used to associate elastic ip on host instance startup, and run certbot cfn on ecs container startup.

        :default: - latest

        :stability: experimental
        '''
        result = self._values.get("aws_cli_docker_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certbot_docker_tag(self) -> typing.Optional[builtins.str]:
        '''(experimental) Docker image tag of certbot/dns-route53 to create certificates.

        :default: - v1.29.0

        :stability: experimental
        :link: https://hub.docker.com/r/certbot/dns-route53/tags
        '''
        result = self._values.get("certbot_docker_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certbot_schedule_interval(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Certbot task schedule interval in days to renew the certificate.

        :default: - 60

        :stability: experimental
        '''
        result = self._values.get("certbot_schedule_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def container_insights(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Enable container insights or not.

        :default: - undefined (container insights disabled)

        :stability: experimental
        '''
        result = self._values.get("container_insights")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def host_instance_spot_price(self) -> typing.Optional[builtins.str]:
        '''(experimental) The maximum hourly price (in USD) to be paid for any Spot Instance launched to fulfill the request.

        Host instance asg would use spot instances if hostInstanceSpotPrice is set.

        :default: - undefined

        :stability: experimental
        :link: https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.AddCapacityOptions.html#spotprice
        '''
        result = self._values.get("host_instance_spot_price")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host_instance_type(self) -> typing.Optional[builtins.str]:
        '''(experimental) Instance type of the ECS host instance.

        :default: - t2.micro

        :stability: experimental
        '''
        result = self._values.get("host_instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_group(self) -> typing.Optional[aws_cdk.aws_logs.ILogGroup]:
        '''(experimental) Log group of the certbot task and the aws-cli task.

        :default: - Creates default cdk log group

        :stability: experimental
        '''
        result = self._values.get("log_group")
        return typing.cast(typing.Optional[aws_cdk.aws_logs.ILogGroup], result)

    @builtins.property
    def record_domain_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Domain names for A records to elastic ip of ECS host instance.

        :default: - [ props.hostedZone.zoneName ]

        :stability: experimental
        '''
        result = self._values.get("record_domain_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[aws_cdk.RemovalPolicy]:
        '''(experimental) Removal policy for the file system and log group (if using default).

        :default: - RemovalPolicy.DESTROY

        :stability: experimental
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[aws_cdk.RemovalPolicy], result)

    @builtins.property
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.SecurityGroup]:
        '''(experimental) Security group of the ECS host instance.

        :default: - Creates security group with allowAllOutbound and ingress rule (ipv4, ipv6) => (tcp 80, 443).

        :stability: experimental
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SecurityGroup], result)

    @builtins.property
    def server_task_definition(
        self,
    ) -> typing.Optional[aws_cdk.aws_ecs.Ec2TaskDefinition]:
        '''(experimental) Task definition for the server ecs task.

        :default: - Nginx server task definition defined in sampleServerTask()

        :stability: experimental
        '''
        result = self._values.get("server_task_definition")
        return typing.cast(typing.Optional[aws_cdk.aws_ecs.Ec2TaskDefinition], result)

    @builtins.property
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''(experimental) Vpc of the ECS host instance and cluster.

        :default: - Creates vpc with only public subnets and no NAT gateways.

        :stability: experimental
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LowCostECSProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "LowCostECS",
    "LowCostECSProps",
]

publication.publish()
