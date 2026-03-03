# Technical Documentation / 技术文档 (S3 Storage Version)

Complete technical guide for deployment, development, and troubleshooting.

完整的部署、开发和故障排查技术指南。

> **Note**: This version uses S3 for data storage.

---

## 📋 Table of Contents / 目录

- [Deployment / 部署](#deployment--部署)
- [Scripts Guide / 脚本指南](#scripts-guide--脚本指南)
- [Troubleshooting / 故障排查](#troubleshooting--故障排查)
- [API Limits / API 限制](#api-limits--api-限制)
- [AWS Events / AWS 事件](#aws-events--aws-事件)

---

## Deployment / 部署

### Prerequisites / 前置要求

- AWS Account with Support plan / 有支持计划的 AWS 账户
- AWS CLI configured / 已配置 AWS CLI
- Python 3.12+ / Python 3.12+（Lambda runtime）
- Node.js 18+ (for CDK) / Node.js 18+（用于 CDK）
- Lark App credentials / Lark应用凭证

### Quick Deployment / 快速部署

```bash
# 1. Deploy infrastructure / 部署基础设施
./deploy.sh

# Or with custom auto-dissolve time / 或自定义自动解散时间
./deploy.sh --auto-dissolve-hours 48

# 2. Configure bot / 配置 Bot
cp accounts-example.json accounts.json
# Edit accounts.json with your Lark credentials and AWS accounts
vim accounts.json
python3 setup_lark_bot.py setup

# 3. Configure Lark webhook / 配置Lark Webhook
# Use URL from setup output / 使用 setup 输出的 URL

# 4. Test in Lark / 在Lark中测试
# Send "帮助" or "help" to bot
```

**What `setup_lark_bot.py setup` does / setup 做什么:**
1. Updates Lark credentials in Secrets Manager / 更新 Secrets Manager 中的 Lark 凭证
2. Creates IAM roles in all accounts for Support API access / 在所有账号创建 Support API 访问角色
3. **Sets up cross-account EventBridge** to forward Support case updates / **设置跨账号 EventBridge** 转发工单更新
4. Initializes S3 configuration with account mappings / 初始化 S3 配置和账号映射

This ensures bidirectional sync works automatically / 确保双向同步自动工作:
- Lark → AWS Support (via Lambda / 通过 Lambda)
- AWS Support → Lark (via EventBridge / 通过 EventBridge)

### Detailed Steps / 详细步骤

#### Step 1: Clone Repository / 克隆仓库

```bash
git clone <repository-url>
cd lark_case_bot_py
```

#### Step 2: Install Dependencies / 安装依赖

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

#### Step 3: Deploy Stack / 部署 Stack

```bash
./deploy.sh
```

**CDK Parameters / CDK 参数**:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `CaseLanguage` | `zh` | AWS Support case language (zh/ja/ko/en) |
| `CasePollInterval` | `10` | Case status polling interval in minutes (1-60) |
| `UserWhitelist` | `false` | Enable user whitelist feature |
| `AllowedAccountIds` | `""` | Comma-separated account IDs for cross-account access |

Example with parameters / 带参数示例:

```bash
cdk deploy \
  --parameters CaseLanguage=en \
  --parameters CasePollInterval=5 \
  --parameters AllowedAccountIds="123456789012,987654321098"
```

This creates / 这将创建：

- Lambda functions (MsgEventLambda, CaseUpdateLambda, CasePollerLambda, GroupCleanupLambda)
- API Gateway (Webhook endpoint)
- S3 bucket (DataBucket for config and case storage)
- EventBridge rules (Case update notifications, scheduled polling, group cleanup)
- Secrets Manager (App ID and Secret storage)
- IAM roles and policies

#### Step 4: Configure Bot / 配置 Bot

```bash
# Using config file (recommended) / 使用配置文件（推荐）
python setup_lark_bot.py setup --config accounts.json

# Or using command line / 或使用命令行
python setup_lark_bot.py setup \
  --app-id cli_xxxxx \
  --app-secret xxxxx \
  --region us-east-1
```

This configures / 这将配置：
- Updates Secrets Manager / 更新 Secrets Manager
- Initializes S3 config / 初始化 S3 配置
- Creates IAM role for Support API / 创建 Support API IAM 角色

#### Step 5: Configure Lark / 配置Lark

1. Go to [Lark Open Platform](https://open.larksuite.com/app)
2. Configure webhook URL (from setup-bot.py output)
3. Subscribe to events:
   - `im.message.receive_v1`
   - `card.action.trigger`
4. Set permissions:
   - `im:message`
   - `im:message.file:readonly`
   - `im:resource:readonly`
   - `im:chat`

#### Step 6: Test / 测试

```bash
# Test webhook
./test-webhook.sh

# Test in Lark
# Send "帮助" or "help" to bot
```

---

## Scripts Guide / 脚本指南

### deploy.sh - Full Deployment / 完整部署

**Purpose / 用途**: Deploy complete CDK stack / 部署完整 CDK Stack

**Deployment Target / 部署目标**:

> ⚠️ **重要**: 此 Stack 必须部署到 `us-east-1` 区域（已硬编码）
>
> - AWS Support API 只在 us-east-1 可用
> - AWS Support EventBridge 事件只发送到 us-east-1
> - 部署到其他区域将导致 EventBridge 通知无法工作

- 区域已硬编码为 `us-east-1`
- 部署到 AWS CLI 配置的默认账号
- 查看当前账号: `aws sts get-caller-identity`
- 使用指定 Profile: `AWS_PROFILE=myprofile ./deploy.sh`

**When to use / 何时使用**:

- ✅ First deployment / 首次部署
- ✅ Infrastructure changes / 基础设施变更
- ❌ Code-only changes / 仅代码变更（使用 deploy-all-lambdas.sh）

**Usage / 使用**:

```bash
# Deploy to default account (region is hardcoded to us-east-1)
./deploy.sh

# Deploy to specific AWS profile
AWS_PROFILE=production ./deploy.sh
```

**Time / 时间**: 3-5 minutes / 3-5 分钟

---

### setup_lark_bot.py - Bot Configuration / Bot 配置

**Purpose / 用途**: Automate bot configuration / 自动化 Bot 配置

**When to use / 何时使用**:

- ✅ After deploy.sh / deploy.sh 之后
- ✅ Update credentials / 更新凭证
- ✅ Reinitialize config / 重新初始化配置

**Usage / 使用**:

```bash
# Using config file (recommended) / 使用配置文件（推荐）
python setup_lark_bot.py setup --config accounts.json

# Using command line / 使用命令行
python setup_lark_bot.py setup --app-id cli_xxxxx --app-secret xxxxx

# Skip IAM role creation / 跳过 IAM 角色创建
python setup_lark_bot.py setup --config accounts.json --skip-iam

# Add accounts / 添加账号
python setup_lark_bot.py accounts add --config accounts.json

# Verify configuration / 验证配置
python setup_lark_bot.py verify --all
```

**Time / 时间**: 1 minute / 1 分钟

---

### scripts/deploy-all-lambdas.sh - Quick Lambda Update / 快速 Lambda 更新

**Purpose / 用途**: Update Lambda code only / 仅更新 Lambda 代码

**When to use / 何时使用**:

- ✅ Code changes / 代码修改
- ✅ Bug fixes / Bug 修复
- ✅ Feature additions / 功能添加

**Usage / 使用**:

```bash
./scripts/deploy-all-lambdas.sh
```

**Time / 时间**: 10-30 seconds / 10-30 秒

---

### Comparison / 对比

| Feature / 特性 | deploy.sh | deploy-all-lambdas.sh |
|---------------|-----------|----------------------|
| Scope / 范围 | Full stack / 完整 Stack | Lambda only / 仅 Lambda |
| Time / 时间 | 3-5 min / 3-5 分钟 | 10-30 sec / 10-30 秒 |
| CloudFormation | ✅ Updates / 更新 | ❌ No change / 不变 |
| Infrastructure / 基础设施 | ✅ Supported / 支持 | ❌ Not supported / 不支持 |
| Code / 代码 | ✅ Supported / 支持 | ✅ Supported / 支持 |

---

## Troubleshooting / 故障排查

For the full troubleshooting guide, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

完整的故障排查指南请参考 [TROUBLESHOOTING.md](TROUBLESHOOTING.md)。

---

## API Limits / API 限制

### Lark Limits / Lark限制

| Item / 项目 | Limit / 限制 |
|------------|-------------|
| Chat name / 群名称 | 100 characters / 100 字符 |
| Text message / 文本消息 | 10,000 characters / 10,000 字符 |
| Rich text / 富文本 | 100,000 characters / 100,000 字符 |
| Card message / 卡片消息 | 30 KB |
| File upload / 文件上传 | 30 MB |
| Image upload / 图片上传 | 30 MB |
| Message rate / 消息频率 | 20/min/user, 50/min/group |

### AWS Support Limits / AWS Support 限制

| Item / 项目 | Limit / 限制 |
|------------|-------------|
| Attachment size / 附件大小 | 5 MB per file / 每文件 5 MB |
| Total attachments / 总附件 | 25 MB per case / 每工单 25 MB |
| API rate / API 频率 | Varies by plan / 根据计划不同 |

### Bot Implementation / Bot 实现

**Chat name generation / 群名称生成**:
```python
# Format: 工单 {ID} - {title}
# Max 100 chars, auto-truncate title if needed
base_name = f"工单 {display_id}"  # ~18 chars
max_title_length = 100 - len(base_name) - 3
if len(subject) > max_title_length:
    truncated_subject = subject[:max_title_length-1] + "…"
```

---

## AWS Events / AWS 事件

### Supported Events / 支持的事件

| Event / 事件 | Notification / 通知 |
|-------------|-------------------|
| `AddCommunicationToCase` (AWS origin) | ✅ Yes / 是 |
| `ResolveCase` | ✅ Yes / 是 |
| `ReopenCase` | ✅ Yes / 是 |
| `CreateCase` | ❌ No (user initiated) / 否（用户发起） |
| Status changes / 状态变化 | ❌ No (AWS limitation) / 否（AWS 限制） |

### Event Structure / 事件结构

```json
{
  "detail": {
    "case-id": "case-xxx",
    "display-id": "176404877500953",
    "event-name": "ResolveCase",
    "communication-id": "",
    "origin": ""
  }
}
```

### Why No Status Change Events? / 为什么没有状态变化事件？

**Reason / 原因**: AWS EventBridge limitation / AWS EventBridge 限制

AWS Support only sends 4 event types:
- CreateCase
- AddCommunicationToCase
- ResolveCase
- ReopenCase

Status changes (pending-customer-action, etc.) are not sent as events.

AWS Support 只发送 4 种事件类型，状态变化不作为事件发送。

---

## Architecture / 架构

### Components / 组件

```text
Lark App
    ↓
API Gateway (Webhook)
    ↓
Lambda (MsgEventLambda)
    ↓
S3 (Config & Cases)
    ↓
AWS Support API
    ↓
EventBridge (Case Updates)          EventBridge (Scheduled)         EventBridge (Hourly)
    ↓                                    ↓                              ↓
Lambda (CaseUpdateLambda)           Lambda (CasePollerLambda)       Lambda (GroupCleanupLambda)
    ↓                                    ↓                              ↓
Lark API (Notifications)            Lark API (Status Updates)       Lark API (Auto-dissolve)
```

### Data Flow / 数据流

**Create Case / 创建工单**:
1. User sends command in Lark / 用户在Lark发送命令
2. Lark sends event to API Gateway / Lark发送事件到 API Gateway
3. Lambda processes and shows card / Lambda 处理并显示卡片
4. User fills card and submits / 用户填写卡片并提交
5. Lambda creates AWS Support case / Lambda 创建 AWS Support 工单
6. Lambda creates Lark group chat / Lambda 创建Lark群聊
7. Lambda sends confirmation / Lambda 发送确认消息

**Case Update / 工单更新**:

1. AWS Support updates case / AWS Support 更新工单
2. EventBridge captures event / EventBridge 捕获事件
3. CaseUpdateLambda processes event / CaseUpdateLambda 处理事件
4. Lambda sends notification to Lark / Lambda 发送通知到Lark

**Case Polling / 工单轮询**:

1. EventBridge triggers CasePollerLambda on schedule / EventBridge 定时触发 CasePollerLambda
2. Lambda queries all tracked cases across accounts / Lambda 查询所有账号的跟踪工单
3. Lambda detects status changes / Lambda 检测状态变化
4. Lambda sends status update to Lark / Lambda 发送状态更新到Lark

**Group Auto-Dissolve / 群自动解散**:

1. EventBridge triggers GroupCleanupLambda hourly / EventBridge 每小时触发 GroupCleanupLambda
2. Lambda scans for resolved cases past dissolve threshold / Lambda 扫描超过解散时限的已解决工单
3. Lambda sends warning message to group / Lambda 发送警告消息到群
4. Lambda dissolves the group chat / Lambda 解散群聊

---

## Development / 开发

### Local Testing / 本地测试

```bash
# Test Lambda function locally
python -c "from lambda.msg_event_handler import lambda_handler; \
  lambda_handler({'body': '{\"type\":\"url_verification\",\"challenge\":\"test\"}'}, None)"
```

### Debug Logging / 调试日志

> **Note**: Lambda function names differ between deployment methods:
> - **CDK**: `LarkCaseBotStack-MsgEventLambda*`, `LarkCaseBotStack-CaseUpdateLambda*`, etc.
> - **Manual**: `LarkCaseBot-MsgEventLambda`, `LarkCaseBot-CaseUpdateLambda`, etc.

```bash
# View Lambda logs (CDK deployment)
aws logs tail /aws/lambda/LarkCaseBotStack-MsgEventLambda* --follow

# View Lambda logs (Manual deployment)
aws logs tail /aws/lambda/LarkCaseBot-MsgEventLambda --follow

# Filter errors (adjust log group name based on deployment type)
aws logs filter-pattern "ERROR" \
  --log-group-name /aws/lambda/LarkCaseBotStack-MsgEventLambda*
```

### Code Structure / 代码结构

```
lambda/
├── msg_event_handler.py      # Main message handler (Lark webhook)
├── case_update_handler.py    # Case update notifications (EventBridge)
├── case_poller.py            # Scheduled case status polling
├── group_cleanup.py          # Auto-dissolve resolved case groups
├── s3_storage.py             # S3 storage helper module
├── i18n.py                   # Multi-language support (zh/en)
└── aws_services_complete.py  # AWS service catalog for case creation
```

---

## Security / 安全

### Data Storage / 数据存储

- Case info: S3 (encrypted at rest)
- Attachments (files and images): Lambda memory (temporary)
- Credentials: Secrets Manager (encrypted)

### Access Control / 访问控制

- IAM roles with least privilege
- Secrets Manager for credentials
- Optional user whitelist

### Compliance / 合规

- AWS data protection policies
- Lark enterprise security standards
- Audit logs in CloudWatch

---

## Performance / 性能

### Lambda Configuration / Lambda 配置

| Lambda | Memory | Timeout | Purpose |
|--------|--------|---------|---------|
| MsgEventLambda | 1024 MB | 60s | Lark webhook, case creation |
| CaseUpdateLambda | 256 MB | 30s | EventBridge notifications |
| CasePollerLambda | 512 MB | 300s | Scheduled status polling |
| GroupCleanupLambda | 256 MB | 300s | Auto-dissolve resolved case groups |

- Concurrency: Auto-scaling

### Optimization / 优化

- Token caching (2 hours)
- Event deduplication (5 minutes)
- Batch API calls when possible

---

## Monitoring / 监控

### CloudWatch Metrics / CloudWatch 指标

- Lambda invocations
- Error rate
- Duration
- Throttles

### Alerts / 告警

- Error rate > 5%
- Duration > 3 seconds
- Throttles > 10/hour

---

## Backup & Recovery / 备份与恢复

### S3 Backup / S3 备份

- S3 versioning enabled
- Cross-region replication available

### Disaster Recovery / 灾难恢复

```bash
# Get bucket name / 获取存储桶名称
# CDK deployment:
BUCKET=$(aws cloudformation describe-stacks --stack-name LarkCaseBotStack \
  --query 'Stacks[0].Outputs[?OutputKey==`DataBucketName`].OutputValue' --output text)
# Manual deployment:
BUCKET="larkcasebot-data-$(aws sts get-caller-identity --query Account --output text)"

# Export S3 data / 导出 S3 数据
aws s3 sync s3://${BUCKET} ./backup/

# Restore if needed / 需要时恢复
aws s3 sync ./backup/ s3://${BUCKET}
```

---

## Upgrade / 升级

### Version Upgrade / 版本升级

```bash
# 1. Backup configuration
aws s3 sync s3://larkcasebotstack-databucket-xxx/config/ ./config_backup/

# 2. Pull latest code
git pull origin main

# 3. Deploy
./deploy.sh

# 4. Verify
./test-webhook.sh
```

---

## FAQ for Developers / 开发者常见问题

### Q: How to add a new command? / 如何添加新命令？

**A**: Edit `msg_event_handler.py`:

```python
# Add command handling
elif text.startswith('新命令') or text.startswith('new command'):
    return handle_new_command(chat_id, user_id)
```

### Q: How to change timezone? / 如何更改时区？

**A**: Edit timezone offset in both Lambda files:

```python
def get_dual_timezone_time() -> str:
    utc_now = datetime.now(timezone.utc)
    # Change hours=8 to your timezone
    local_time = utc_now + timedelta(hours=8)
    # Change GMT+8 to your timezone label
    return f"{utc_str} UTC / {local_str} GMT+8"
```

### Q: How to add more AWS accounts? / 如何添加更多 AWS 账户？

**A**: Update S3 config file (`config/LarkBotProfile-0.json`):

```json
{
  "cfg_key": "LarkBotProfile-0",
  "accounts": {
    "0": {"role_arn": "arn:aws:iam::111111111111:role/Role1", "account_name": "Account 1"},
    "1": {"role_arn": "arn:aws:iam::222222222222:role/Role2", "account_name": "Account 2"}
  }
}
```

---

## Category Selection Logic / Category 选择逻辑

### How It Works / 工作原理

When creating a case, the system automatically selects the best category for the chosen service:

创建工单时，系统会自动为所选服务选择最佳 category：

```
Priority / 优先级:
1. general-guidance  (最优先)
   ↓
2. other            (次优先)
   ↓
3. First category   (后备)
   ↓
4. 'general-guidance' (默认值，API 调用失败时使用)
```

### Implementation / 实现

```python
# Get categories from AWS Support API
categories_response = support_client.describe_services(
    serviceCodeList=[service_code],
    language=CASE_LANGUAGE
)

# Select by priority
if 'general-guidance' in category_codes:
    category_code = 'general-guidance'
elif 'other' in category_codes:
    category_code = 'other'
elif category_codes:
    category_code = category_codes[0]
```

### Retry Logic / 重试逻辑

If case creation fails with `InvalidParameterValueException`, the system retries without the `issueType` parameter:

如果创建工单失败并返回 `InvalidParameterValueException`，系统会不带 `issueType` 参数重试：

```python
try:
    response = support_client.create_case(**create_params)
except InvalidParameterValueException:
    # Retry without issueType
    del create_params['issueType']
    response = support_client.create_case(**create_params)
```

### Service Mapping / 服务映射

Common services and their correct codes:

常用服务及其正确代码：

| Service / 服务 | Service Code | Default Category |
|---------------|-------------|------------------|
| EKS | `service-eks` | `general-guidance` |
| Lambda | `aws-lambda` | `general-guidance` |
| S3 | `amazon-simple-storage-service` | `general-guidance` |
| EC2 (Linux) | `amazon-elastic-compute-cloud-linux` | `general-guidance` |
| DynamoDB | `amazon-dynamodb` | `general-guidance` |
| VPC | `amazon-virtual-private-cloud` | `general-guidance` |

完整服务列表可通过 AWS Support API `describe_services()` 获取。

---

## Advanced Configuration / 高级配置

### 配置文件格式

基础配置文件 `accounts.json`：

```json
{
  "lark": {
    "app_id": "cli_xxxxxxxxxx",
    "app_secret": "your_app_secret_here"
  },
  "aws": {
    "region": "us-east-1"
  },
  "accounts": [
    {
      "account_id": "123456789012",
      "account_name": "生产账号",
      "profile": "default"
    }
  ]
}
```

### 高级配置选项

机器人配置存储在 S3 的 `config/LarkBotProfile-0.json` 中。可通过 `accounts.json` 的 `bot` 块自定义：

```json
{
  "lark": { ... },
  "aws": { ... },
  "accounts": [ ... ],
  
  "bot": {
    "cfg_key": "LarkBotProfile-0",
    "user_whitelist_enabled": false,
    "user_whitelist": {
      "ou_xxxxxx": "张三",
      "ou_yyyyyy": "李四"
    }
  }
}
```

| 字段 | 说明 | 默认值 |
|-----|------|-------|
| `cfg_key` | S3 配置键 | `LarkBotProfile-0` |
| `user_whitelist_enabled` | 是否启用用户白名单 | `false` |
| `user_whitelist` | 白名单用户映射 (user_id → 名称) | `{}` |

> **注意**: 消息文本（帮助、错误提示等）通过 `lambda/i18n.py` 管理，支持中英文自动切换。如需自定义消息，请修改 `i18n.py` 文件。

### 用户白名单

启用白名单后，只有白名单中的用户可以创建工单：

1. 在配置文件中设置 `user_whitelist_enabled: true`
2. 添加用户到 `user_whitelist`（key 为 Lark user_id，value 为显示名称）
3. 运行 `python setup_lark_bot.py setup --config accounts.json`

获取用户 ID：在 Lark 开放平台的 API 调试工具中测试消息接收，查看 `sender.sender_id.user_id`。

---

**Last Updated / 最后更新**: 2025-12-04
