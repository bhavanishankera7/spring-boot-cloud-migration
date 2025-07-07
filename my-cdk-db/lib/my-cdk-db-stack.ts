import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as rds from 'aws-cdk-lib/aws-rds';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class MyCdkDbStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create a VPC (or use an existing one)
    const vpc = new ec2.Vpc(this, 'MyVpc', { maxAzs: 2 });

    // Create a security group for the DB
    const dbSecurityGroup = new ec2.SecurityGroup(this, 'DbSecurityGroup', {
      vpc,
      allowAllOutbound: true,
      description: 'Allow PostgreSQL access',
    });

    // Allow inbound PostgreSQL from anywhere (for demo; restrict in production)
    dbSecurityGroup.addIngressRule(ec2.Peer.anyIpv4(), ec2.Port.tcp(5432), 'Allow PostgreSQL');

    // Create the RDS PostgreSQL instance
    new rds.DatabaseInstance(this, 'PostgresInstance', {
      engine: rds.DatabaseInstanceEngine.postgres({ version: rds.PostgresEngineVersion.VER_15 }),
      vpc,
      vpcSubnets: { subnetType: ec2.SubnetType.PUBLIC },
      securityGroups: [dbSecurityGroup],
      instanceType: ec2.InstanceType.of(ec2.InstanceClass.T3, ec2.InstanceSize.MICRO),
      multiAz: false,
      allocatedStorage: 20,
      maxAllocatedStorage: 100,
      databaseName: 'mydb',
      credentials: rds.Credentials.fromGeneratedSecret('postgres'),
      publiclyAccessible: true,
      removalPolicy: cdk.RemovalPolicy.DESTROY, // NOT for production!
      deletionProtection: false,
    });

    // The code that defines your stack goes here

    // example resource
    // const queue = new sqs.Queue(this, 'MyCdkDbQueue', {
    //   visibilityTimeout: cdk.Duration.seconds(300)
    // });
  }
}
