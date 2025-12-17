"""
AWS Support Complete Service List

This module contains the complete list of AWS services with their Support API
service codes and display names, organized by category.

Features:
- Complete AWS service catalog for Support case creation
- Service categorization (Compute, Storage, Database, Network, etc.)
- Issue type definitions (technical, customer-service, account-and-billing)
- Cost Explorer service name to Support code mapping
- Helper functions for service filtering and merging

Usage:
    from aws_services_complete import (
        get_all_services_flat,
        get_services_for_issue_type,
        merge_with_cost_explorer_services,
        CE_TO_SUPPORT_MAPPING
    )
    
    # Get all services as flat list
    services = get_all_services_flat()
    
    # Get services for specific issue type
    billing_services = get_services_for_issue_type('account-and-billing')
"""

# Complete AWS service list (grouped by category)
AWS_SERVICES_COMPLETE = {
    "Compute Services": [
        {"code": "amazon-elastic-compute-cloud-linux", "name": "EC2 (Linux)", "category": "general-guidance"},
        {"code": "amazon-elastic-compute-cloud-windows", "name": "EC2 (Windows)", "category": "general-guidance"},
        {"code": "aws-lambda", "name": "Lambda", "category": "general-guidance"},
        {"code": "ec2-container-service", "name": "ECS", "category": "general-guidance"},
        {"code": "service-eks", "name": "EKS", "category": "general-guidance"},
        {"code": "amazon-batch", "name": "Batch", "category": "general-guidance"},
        {"code": "aws-elastic-beanstalk", "name": "Elastic Beanstalk", "category": "general-guidance"},
        {"code": "amazon-lightsail", "name": "Lightsail", "category": "general-guidance"},
    ],
    
    "Storage Services": [
        {"code": "amazon-simple-storage-service", "name": "S3", "category": "general-guidance"},
        {"code": "amazon-elastic-block-store", "name": "EBS", "category": "general-guidance"},
        {"code": "amazon-elastic-file-system", "name": "EFS", "category": "general-guidance"},
        {"code": "aws-storage-gateway", "name": "Storage Gateway", "category": "general-guidance"},
        {"code": "service-fsx-for-lustre", "name": "FSx for Lustre", "category": "general-guidance"},
        {"code": "service-fsx-for-windows-file-server", "name": "FSx for Windows", "category": "general-guidance"},
        {"code": "service-backup", "name": "Backup", "category": "general-guidance"},
    ],
    
    "Database Services": [
        {"code": "amazon-dynamodb", "name": "DynamoDB", "category": "general-guidance"},
        {"code": "amazon-relational-database-service-mysql", "name": "RDS MySQL", "category": "general-guidance"},
        {"code": "amazon-relational-database-service-postgresql", "name": "RDS PostgreSQL", "category": "general-guidance"},
        {"code": "amazon-relational-database-service-aurora", "name": "Aurora MySQL", "category": "general-guidance"},
        {"code": "amazon-relational-database-service-aurora-postgres", "name": "Aurora PostgreSQL", "category": "general-guidance"},
        {"code": "amazon-elasticache", "name": "ElastiCache", "category": "general-guidance"},
        {"code": "amazon-redshift", "name": "Redshift", "category": "general-guidance"},
        {"code": "service-documentdb-with-mongodb-compatibility", "name": "DocumentDB", "category": "general-guidance"},
        {"code": "neptune", "name": "Neptune", "category": "general-guidance"},
        {"code": "service-timestream", "name": "Timestream", "category": "general-guidance"},
        {"code": "service-managed-apache-cassandra-service", "name": "Keyspaces", "category": "general-guidance"},
    ],
    
    "Network Services": [
        {"code": "amazon-virtual-private-cloud", "name": "VPC", "category": "general-guidance"},
        {"code": "amazon-cloudfront", "name": "CloudFront", "category": "general-guidance"},
        {"code": "amazon-route53", "name": "Route 53", "category": "general-guidance"},
        {"code": "aws-direct-connect", "name": "Direct Connect", "category": "general-guidance"},
        {"code": "elastic-load-balancing", "name": "ELB/ALB/NLB", "category": "general-guidance"},
        {"code": "api-gateway", "name": "API Gateway", "category": "general-guidance"},
        {"code": "service-vpc-transit-gateway", "name": "Transit Gateway", "category": "general-guidance"},
        {"code": "service-global-accelerator", "name": "Global Accelerator", "category": "general-guidance"},
    ],
    
    "Security Services": [
        {"code": "aws-identity-and-access-management", "name": "IAM", "category": "general-guidance"},
        {"code": "key-management-service", "name": "KMS", "category": "general-guidance"},
        {"code": "secrets-manager", "name": "Secrets Manager", "category": "general-guidance"},
        {"code": "amazon-acm-service", "name": "ACM", "category": "general-guidance"},
        {"code": "amazon-cognito", "name": "Cognito", "category": "general-guidance"},
        {"code": "aws-web-application-firewall", "name": "WAF", "category": "general-guidance"},
        {"code": "aws-shield", "name": "Shield", "category": "general-guidance"},
        {"code": "guardduty", "name": "GuardDuty", "category": "general-guidance"},
        {"code": "aws-inspector", "name": "Inspector", "category": "general-guidance"},
        {"code": "service-security-hub", "name": "Security Hub", "category": "general-guidance"},
    ],
    
    "Monitoring and Management": [
        {"code": "amazon-cloudwatch", "name": "CloudWatch", "category": "general-guidance"},
        {"code": "cloudtrail", "name": "CloudTrail", "category": "general-guidance"},
        {"code": "config-service", "name": "Config", "category": "general-guidance"},
        {"code": "systems-manager", "name": "Systems Manager", "category": "general-guidance"},
        {"code": "aws-cloudformation", "name": "CloudFormation", "category": "general-guidance"},
        {"code": "service-catalog", "name": "Service Catalog", "category": "general-guidance"},
        {"code": "aws-trusted-advisor", "name": "Trusted Advisor", "category": "general-guidance"},
        {"code": "aws-organizations", "name": "Organizations", "category": "general-guidance"},
    ],
    
    "Analytics Services": [
        {"code": "amazon-athena", "name": "Athena", "category": "general-guidance"},
        {"code": "aws-glue", "name": "Glue", "category": "general-guidance"},
        {"code": "amazon-elastic-mapreduce", "name": "EMR", "category": "general-guidance"},
        {"code": "amazon-kinesis", "name": "Kinesis", "category": "general-guidance"},
        {"code": "amazon-quicksight", "name": "QuickSight", "category": "general-guidance"},
        {"code": "service-managed-streaming-for-kafka", "name": "MSK", "category": "general-guidance"},
        {"code": "aws-data-pipeline", "name": "Data Pipeline", "category": "general-guidance"},
    ],
    
    "Application Integration": [
        {"code": "amazon-simple-notification-service", "name": "SNS", "category": "general-guidance"},
        {"code": "amazon-simple-queue-service", "name": "SQS", "category": "general-guidance"},
        {"code": "service-eventbridge", "name": "EventBridge", "category": "general-guidance"},
        {"code": "aws-step-functions", "name": "Step Functions", "category": "general-guidance"},
        {"code": "service-appflow", "name": "AppFlow", "category": "general-guidance"},
    ],
    
    "Developer Tools": [
        {"code": "codecommit", "name": "CodeCommit", "category": "general-guidance"},
        {"code": "amazon-codebuild", "name": "CodeBuild", "category": "general-guidance"},
        {"code": "codedeploy", "name": "CodeDeploy", "category": "general-guidance"},
        {"code": "codepipeline", "name": "CodePipeline", "category": "general-guidance"},
        {"code": "cloud9", "name": "Cloud9", "category": "general-guidance"},
        {"code": "amazon-xray", "name": "X-Ray", "category": "general-guidance"},
    ],
    
    "Machine Learning": [
        {"code": "sagemaker", "name": "SageMaker", "category": "general-guidance-custom-algorithm"},
        {"code": "amazon-rekognition", "name": "Rekognition", "category": "general-guidance"},
        {"code": "comprehend", "name": "Comprehend", "category": "general-guidance"},
        {"code": "translate", "name": "Translate", "category": "general-guidance"},
        {"code": "amazon-polly", "name": "Polly", "category": "general-guidance"},
        {"code": "transcribe", "name": "Transcribe", "category": "general-guidance"},
        {"code": "amazon-lex", "name": "Lex", "category": "general-guidance"},
        {"code": "service-bedrock", "name": "Bedrock", "category": "general-guidance"},
    ],
    
    "Other Services": [
        {"code": "general-info", "name": "General Info", "category": "using-aws"},
        {"code": "billing", "name": "Billing", "category": "other-billing-questions"},
        {"code": "customer-account", "name": "Account", "category": "other-account-issues"},
    ],
}

# Issue type definitions
ISSUE_TYPES = {
    "technical": {
        "name": "🔧 Technical Support",
        "description": "Technical issues, service failures, configuration help",
        "services": "all"  # Can select all services
    },
    "customer-service": {
        "name": "👤 Customer Service",
        "description": "Account related, service limits, general inquiries",
        "services": ["general-info", "customer-account"]
    },
    "account-and-billing": {
        "name": "💰 Billing Issues",
        "description": "Billing issues, cost inquiries, account management",
        "services": ["billing", "customer-account", "general-info"]
    }
}


def get_all_services_flat():
    """Get all services as a flat list"""
    all_services = []
    for category, services in AWS_SERVICES_COMPLETE.items():
        all_services.extend(services)
    return all_services


def get_services_by_category():
    """Get services by category"""
    return AWS_SERVICES_COMPLETE


def get_services_for_issue_type(issue_type: str):
    """Get available services list based on issue type"""
    issue_config = ISSUE_TYPES.get(issue_type, {})
    allowed_services = issue_config.get("services", "all")
    
    if allowed_services == "all":
        return get_all_services_flat()
    else:
        # Only return allowed services
        all_services = get_all_services_flat()
        return [s for s in all_services if s["code"] in allowed_services]


def merge_with_cost_explorer_services(ce_services, all_services):
    """
    Merge Cost Explorer services with complete service list
    Services discovered from Cost Explorer are placed first, marked as "recently used"
    """
    # Service codes from Cost Explorer
    ce_codes = {s["code"] for s in ce_services}
    
    # Recently used services (placed first)
    recent_services = []
    for service in ce_services:
        service_copy = service.copy()
        service_copy["name"] = f"{service['name']} (Recently Used)"
        service_copy["recent"] = True
        recent_services.append(service_copy)
    
    # Other services (placed after)
    other_services = []
    for service in all_services:
        if service["code"] not in ce_codes:
            service_copy = service.copy()
            service_copy["recent"] = False
            other_services.append(service_copy)
    
    # Merge: recently used + separator + other services
    return recent_services, other_services


# Cost Explorer service name to Support code mapping
CE_TO_SUPPORT_MAPPING = {
    'Amazon Elastic Compute Cloud - Compute': ('amazon-elastic-compute-cloud-linux', 'EC2'),
    'Amazon Simple Storage Service': ('amazon-simple-storage-service', 'S3'),
    'AWS Lambda': ('aws-lambda', 'Lambda'),
    'Amazon DynamoDB': ('amazon-dynamodb', 'DynamoDB'),
    'Amazon Relational Database Service': ('amazon-relational-database-service-mysql', 'RDS'),
    'Amazon Virtual Private Cloud': ('amazon-virtual-private-cloud', 'VPC'),
    'AWS Glue': ('aws-glue', 'Glue'),
    'Amazon Athena': ('amazon-athena', 'Athena'),
    'AWS Config': ('config-service', 'Config'),
    'AWS Key Management Service': ('key-management-service', 'KMS'),
    'AWS Secrets Manager': ('secrets-manager', 'Secrets Manager'),
    'Amazon Route 53': ('amazon-route53', 'Route 53'),
    'Amazon CloudFront': ('amazon-cloudfront', 'CloudFront'),
    'Amazon Elastic Container Service': ('ec2-container-service', 'ECS'),
    'Amazon Elastic Kubernetes Service': ('service-eks', 'EKS'),
    'Amazon Simple Notification Service': ('amazon-simple-notification-service', 'SNS'),
    'Amazon Simple Queue Service': ('amazon-simple-queue-service', 'SQS'),
    'Amazon ElastiCache': ('amazon-elasticache', 'ElastiCache'),
    'Amazon Redshift': ('amazon-redshift', 'Redshift'),
    'Amazon CloudWatch': ('amazon-cloudwatch', 'CloudWatch'),
    'AWS CloudTrail': ('cloudtrail', 'CloudTrail'),
    'Amazon API Gateway': ('api-gateway', 'API Gateway'),
    'AWS Step Functions': ('aws-step-functions', 'Step Functions'),
    'Amazon Kinesis': ('amazon-kinesis', 'Kinesis'),
    'Amazon EMR': ('amazon-elastic-mapreduce', 'EMR'),
    'Amazon SageMaker': ('sagemaker', 'SageMaker'),
    'AWS CodeBuild': ('amazon-codebuild', 'CodeBuild'),
    'AWS CodePipeline': ('codepipeline', 'CodePipeline'),
    'Amazon Cognito': ('amazon-cognito', 'Cognito'),
    'AWS WAF': ('aws-web-application-firewall', 'WAF'),
    'Amazon GuardDuty': ('guardduty', 'GuardDuty'),
    'AWS Systems Manager': ('systems-manager', 'Systems Manager'),
    'AWS CloudFormation': ('aws-cloudformation', 'CloudFormation'),
    'Amazon Bedrock': ('service-bedrock', 'Bedrock'),
}
