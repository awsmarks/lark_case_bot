"""
Internationalization (i18n) Module for Lark Case Bot
i18n Module - Multi-language Support

This module provides multi-language support for the Lark Case Bot.

Supported Languages:
- zh (Chinese): Chinese - Default language
- en (English): English

Features:
- Automatic language detection from Lark user settings
- Command matching in multiple languages
- Localized error messages and help text
- Fallback to default language if not detected

Usage:
    from i18n import get_message, get_user_language, match_command, DEFAULT_LANGUAGE
    
    # Get localized message
    msg = get_message('zh', 'no_permission')
    
    # Detect user language
    lang = get_user_language(open_id='xxx', token_func=get_token)
    
    # Match command in any language
    matched, lang, remaining = match_command('create case test', 'create_case')
"""

# ============================================================
# 默认语言设置 / Default Language Setting
# ============================================================
# 可选值 / Options: 'zh' (中文), 'en' (English)
# 修改此值可更改系统默认语言
# Change this value to set the system default language
DEFAULT_LANGUAGE = 'zh'
# ============================================================

# Language mappings
MESSAGES = {
    'zh': {
        # Commands
        'create_case': '开工单',
        'reply_case': '回复工单',
        'history': '历史',
        'follow': '关注',
        'help': '帮助',
        'upload': '上传',
        'dissolve': '解散',
        'dissolve_group': '解散群',

        # Error messages
        'no_permission': '❌ 你没有权限使用此机器人',
        'enter_title': '❌ 请输入工单标题\n\n格式: 开工单 [标题]',
        'enter_case_id': '❌ 请输入工单ID\n\n格式: 关注 [工单ID]',
        'case_not_found': '❌ 未找到工单 {}\n\n请确认工单 ID 是否正确',
        'reply_in_case_chat': '❌ "回复工单" 命令只能在工单群中使用\n\n💡 请在相应的工单群中发送此命令',
        'enter_reply_content': '❌ 请输入回复内容\n\n格式: 回复工单 [内容]',
        'reply_empty': '❌ 回复内容不能为空\n\n格式: 回复工单 [内容]',
        'upload_in_case_chat': '❌ 请在工单群中上传附件',
        'file_received': '📎 收到文件: {}',
        'file_upload_hint': '💡 如需上传到 AWS 工单，请回复此文件消息并输入 "上传" 或 "upload"',
        'image_received': '📷 收到图片',
        'image_upload_hint': '💡 如需上传到 AWS 工单，请回复此图片消息并输入 "上传" 或 "upload"',
        
        # File upload messages
        'upload_reply_to_file': '❌ 请回复一条文件或图片消息并输入 "上传" 或 "upload"',
        'upload_get_msg_failed': '❌ 无法获取原始消息内容，请重试',
        'upload_no_account_info': '❌ 配置错误: 未找到此工单的 AWS 账户信息',
        'upload_success': '✅ 附件 {} 已上传到工单 {}',
        'upload_add_failed': '❌ 附件上传失败: 无法添加到工单通信',
        'upload_failed': '❌ 附件 "{}" 上传失败，请稍后重试',
        'upload_expired': '❌ 附件下载失败: 文件可能已过期或无访问权限\n\n💡 请尝试重新上传文件',
        'upload_no_permission': '❌ 附件下载失败: 机器人无访问权限\n\n💡 请检查机器人权限设置',
        'upload_not_found': '❌ 附件下载失败: 文件未找到\n\n💡 请重新上传文件',
        'upload_error': '❌ 附件处理失败\n\n错误: {}\n\n💡 请稍后重试或联系管理员',
        
        # Dissolve group messages
        'dissolve_not_case_chat': '❌ 这不是工单群，无法解散',
        'dissolve_only_creator': '❌ 只有工单创建者 ({}) 才能解散此群',
        'dissolve_warning': '⚠️ 正在解散工单群...\n\n工单ID: {}\n标题: {}\n\n注意: 解散后群聊无法恢复，但工单仍存在于 AWS Support 中。',
        'dissolve_failed': '❌ 解散群聊失败\n\n错误代码: {}\n错误信息: {}',
        'case_resolved_dissolve_notice': '⏰ 此工单群将在 {} 小时后自动解散。如需继续讨论，请在 AWS Console 中重新打开工单。',
        
        # Success messages
        'added_to_chat': '✅ 已将你添加到工单群 {}',
        'already_in_chat': 'ℹ️ 你已在工单群 {} 中，请查看你的群聊列表',
        'reply_sent': '✅ 回复已发送到 AWS Support',
        'file_uploaded': '✅ 附件已上传到 AWS Support',
        'case_no_chat': '❌ 工单 {} 没有关联的工单群',
        'unable_get_user_info': '❌ 无法获取用户信息，请稍后重试',
        'add_to_chat_failed': '❌ 添加到工单群失败\n\n错误代码: {}\n错误信息: {}',
        'synced_to_case': '✅ 已同步到工单 {}\n\n{}',
        'sync_failed': '❌ 回复同步失败，请稍后重试\n\n工单: {}',
        'enter_reply_at_bot': '❌ 请输入回复内容\n\n格式: @bot [内容]',
        'config_no_account': '❌ 配置错误: 未找到此工单的 AWS 账户信息',
        'no_accounts_configured': '❌ 未配置 AWS 账户，请联系管理员',
        'no_history': '📭 暂无工单记录',
        'draft_not_found': '❌ 草稿未找到，请重新开始',
        'select_valid_service': '❌ 请选择有效的服务',
        'select_account': '❌ 请选择 AWS 账户',
        'config_error': '❌ 配置错误，请联系管理员',
        'fill_required_fields': '❌ 请填写以下必填项:\n\n{}',
        'only_creator_can_submit': '只有创建者可以提交此工单',
        
        # Help messages
        'help_title': '🤖 AWS Support Bot 帮助',
        'help_create': '📝 创建工单',
        'help_create_cmd': '• 开工单 [标题] - 创建新的支持工单',
        'help_other': '📋 其他命令',
        'help_history_cmd': '• 历史 - 查询最近10个工单',
        'help_follow_cmd': '• 关注 [工单ID] - 加入指定工单群',
        'help_help_cmd': '• 帮助 - 显示此帮助信息',
        
        # Case chat help
        'case_help_title': '🤖 工单群使用说明',
        'case_help_sync': '💬 同步到 AWS Support',
        'case_help_reply': '• 回复工单 [内容] - 将消息同步到 AWS Support',
        'case_help_upload': '• 上传文件/图片后，回复 "上传" 同步到 AWS Support',
        'case_help_discuss': '💭 群内讨论',
        'case_help_discuss_1': '• 普通消息仅在群内显示，不会同步到 AWS Support',
        'case_help_discuss_2': '• 适合团队内部讨论问题',
        'case_help_notify': '📢 通知',
        'case_help_notify_1': '• AWS Support 工程师的回复会自动推送到此群',
        'case_help_more': '• 输入 帮助 查看更多命令',
        
        # Severity levels
        'severity_low': '一般性指导',
        'severity_normal': '系统受损',
        'severity_high': '生产系统受损',
        'severity_urgent': '生产系统宕机',
        'severity_critical': '业务关键系统宕机',
        
        # Case detail labels
        'label_case_id': '案例ID',
        'label_title': '标题',
        'label_account': '账户',
        'label_severity': '严重程度',
        'label_created_time': '创建时间',
        'label_created_by': '创建人',
        'label_case_creator': '工单创建者',
        
        # Case chat instructions
        'sync_to_support': '同步到 AWS Support',
        'sync_instruction': '@bot [内容]',
        'sync_description': ' - 将消息同步到 AWS Support',
        'upload_attachment': '上传文件/图片',
        'upload_description': ' - 回复 "上传" 同步到 AWS Support',
        'internal_discussion': '群内讨论',
        'internal_discussion_1': '• 普通消息（不 @bot）仅在群内显示，不会同步到 AWS Support',
        'internal_discussion_2': '• 适合团队内部讨论问题',
        'notification': '通知',
        'notification_1': '• AWS Support 工程师的回复会自动推送到此群',
        'type_help': '• 输入 ',
        'see_more_commands': ' 查看更多命令',
        
        # Case creation
        'case_create_failed': '❌ 创建失败: {}',
        'case_details_title': 'AWS 支持工单详情',
        
        # Card UI
        'card_header': '创建 AWS Support 工单',
        'card_aws_account': 'AWS 账户',
        'card_select_account': '选择 AWS 账户',
        'card_case_title': '工单标题',
        'card_aws_service': 'AWS 服务',
        'card_select_service': '选择 AWS 服务',
        'card_severity': '严重程度',
        'card_select_severity': '选择严重程度',
        'card_submit': '提交工单',
        'card_all_services': '─────── 所有服务 ───────',
        'card_severity_low': '⚪ 一般性指导 - 24小时响应',
        'card_severity_normal': '🟡 系统受损 - 12小时响应',
        'card_severity_high': '🟠 生产系统受损 - 4小时响应',
        'card_severity_urgent': '🔴 生产系统宕机 - 1小时响应',
        'card_severity_critical': '🔴 业务关键系统宕机 - 15分钟响应',
        'card_issue_technical': '🔧 技术支持',
        'card_issue_billing': '💰 账单问题',
        'card_issue_service': '👤 客户服务',
        'card_assistant_title': 'AWS Support 工单助手',
        'card_create_flow': '📝 **创建工单流程**',
        'card_create_step1': '1. 在卡片中选择 AWS 账户、服务类型和严重程度',
        'card_create_step2': '2. 点击"提交工单"按钮',
        'card_create_step3': '3. 机器人会自动创建专属工单群',
        'card_communication': '💬 **工单沟通**',
        'card_comm_sync': '• 在工单群中 **@bot [内容]** 同步到 AWS Support',
        'card_comm_upload': '• 上传文件/图片后，回复 "上传" 同步到工单',
        'card_comm_internal': '• 普通消息仅供内部讨论',
        'card_tips': '💡 **问题描述建议**',
        'card_tip1': '• 问题发生的时间和时区',
        'card_tip2': '• 涉及的资源 ID 和区域',
        'card_tip3': '• 问题症状和业务影响',
        'card_tip4': '• 联系人和联系方式',
        
        # Success messages (for original chat)
        'case_created_success': '✅ AWS Support 工单创建成功！',
        'case_account_label': '账户',
        'case_id_label': '工单ID',
        'case_issue_type_label': '问题类型',
        'case_title_label': '标题',
        'case_severity_label': '严重程度',
        'case_chat_created': '已创建专属工单群，更新将在那里通知',
        'case_join_instruction': '其他人可通过',
        'case_join_suffix': '加入工单群',
        
        # Case poller messages
        'poller_message_truncated': '[消息已截断，请查看 AWS Console]',
        'poller_case_reply': '工单回复',
        'poller_case_label': '工单',
        'poller_status_update': '工单状态更新',
        'poller_new_status': '新状态',
        
        # Case status
        'status_opened': '🟢 已开启',
        'status_pending_customer': '🟡 等待客户操作',
        'status_customer_completed': '🟢 客户操作已完成',
        'status_reopened': '🔵 已重新开启',
        'status_resolved': '✅ 已解决',
        'status_unassigned': '⚪ 未分配',
        'status_in_progress': '🔄 处理中',
    },
    
    'en': {
        # Commands
        'create_case': 'create case',
        'reply_case': 'reply case',
        'history': 'history',
        'follow': 'follow',
        'help': 'help',
        'upload': 'upload',
        'dissolve': 'dissolve',
        'dissolve_group': 'dissolve group',
        
        # Error messages
        'no_permission': '❌ You do not have permission to use this bot',
        'enter_title': '❌ Please enter case title\n\nFormat: create case [title]',
        'enter_case_id': '❌ Please enter case ID\n\nFormat: follow [case ID]',
        'case_not_found': '❌ Case {} not found\n\nPlease verify the case ID',
        'reply_in_case_chat': '❌ "reply case" command can only be used in case chats\n\n💡 Please send this command in the relevant case chat',
        'enter_reply_content': '❌ Please enter reply content\n\nFormat: reply case [content]',
        'reply_empty': '❌ Reply content cannot be empty\n\nFormat: reply case [content]',
        'upload_in_case_chat': '❌ Please upload files in case chat',
        'file_received': '📎 File received: {}',
        'file_upload_hint': '💡 To upload to AWS case, reply to this file message with "upload"',
        'image_received': '📷 Image received',
        'image_upload_hint': '💡 To upload to AWS case, reply to this image message with "upload"',
        
        # File upload messages
        'upload_reply_to_file': '❌ Please reply to a file or image message with "upload"',
        'upload_get_msg_failed': '❌ Unable to get original message content, please retry',
        'upload_no_account_info': '❌ Config error: No AWS account info found for this case',
        'upload_success': '✅ Attachment {} uploaded to case {}',
        'upload_add_failed': '❌ Attachment upload failed: Unable to add to case communication',
        'upload_failed': '❌ Attachment "{}" upload failed, please try again later',
        'upload_expired': '❌ Attachment download failed: File may have expired or no access permission\n\n💡 Please try uploading the file again',
        'upload_no_permission': '❌ Attachment download failed: Bot has no access permission\n\n💡 Please check Bot permission settings',
        'upload_not_found': '❌ Attachment download failed: File not found\n\n💡 Please upload the file again',
        'upload_error': '❌ Attachment processing failed\n\nError: {}\n\n💡 Please try again later or contact admin',
        
        # Dissolve group messages
        'dissolve_not_case_chat': '❌ This is not a case chat, cannot dissolve',
        'dissolve_only_creator': '❌ Only case creator ({}) can dissolve this chat',
        'dissolve_warning': '⚠️ Dissolving case chat...\n\nCase ID: {}\nSubject: {}\n\nNote: Once dissolved, the chat cannot be recovered, but the case still exists in AWS Support.',
        'dissolve_failed': '❌ Failed to dissolve group\n\nError code: {}\nError message: {}',
        'case_resolved_dissolve_notice': '⏰ This case chat will be auto-dissolved in {} hours. To continue discussion, please reopen the case in AWS Console.',
        
        # Success messages
        'added_to_chat': '✅ You have been added to the case chat for {}',
        'already_in_chat': 'ℹ️ You are already in the case chat for {}, please check your chat list',
        'reply_sent': '✅ Reply sent to AWS Support',
        'file_uploaded': '✅ File uploaded to AWS Support',
        'case_no_chat': '❌ Case {} has no associated case chat',
        'unable_get_user_info': '❌ Unable to get user info, please try again later',
        'add_to_chat_failed': '❌ Failed to add to case chat\n\nError code: {}\nError message: {}',
        'synced_to_case': '✅ Synced to case {}\n\n{}',
        'sync_failed': '❌ Reply sync failed, please try again later\n\nCase: {}',
        'enter_reply_at_bot': '❌ Please enter reply content\n\nFormat: @bot [content]',
        'config_no_account': '❌ Config error: No AWS account info found for this case',
        'no_accounts_configured': '❌ No AWS accounts configured, please contact admin',
        'no_history': '📭 No case history',
        'draft_not_found': '❌ Draft not found, please start over',
        'select_valid_service': '❌ Please select a valid service',
        'select_account': '❌ Please select an AWS account',
        'config_error': '❌ Config error, please contact admin',
        'fill_required_fields': '❌ Please fill in the following required fields:\n\n{}',
        'only_creator_can_submit': 'Only the creator can submit this case',
        
        # Help messages
        'help_title': '🤖 AWS Support Bot Help',
        'help_create': '📝 Create Case',
        'help_create_cmd': '• create case [title] - Create new support case',
        'help_other': '📋 Other Commands',
        'help_history_cmd': '• history - Query recent 10 cases',
        'help_follow_cmd': '• follow [case ID] - Join specified case chat',
        'help_help_cmd': '• help - Show this help message',
        
        # Case chat help
        'case_help_title': '🤖 Case Chat Instructions',
        'case_help_sync': '💬 Sync to AWS Support',
        'case_help_reply': '• reply case [content] - Sync message to AWS Support',
        'case_help_upload': '• Send file/image, then reply with "upload" to sync to AWS Support',
        'case_help_discuss': '💭 Internal Discussion',
        'case_help_discuss_1': '• Regular messages stay in chat only, not synced to AWS Support',
        'case_help_discuss_2': '• Good for team internal discussions',
        'case_help_notify': '📢 Notifications',
        'case_help_notify_1': '• AWS Support engineer replies will be pushed here automatically',
        'case_help_more': '• Type help to see more commands',
        
        # Severity levels
        'severity_low': 'General guidance',
        'severity_normal': 'System impaired',
        'severity_high': 'Production system impaired',
        'severity_urgent': 'Production system down',
        'severity_critical': 'Business-critical system down',
        
        # Case detail labels
        'label_case_id': 'Case ID',
        'label_title': 'Title',
        'label_account': 'Account',
        'label_severity': 'Severity',
        'label_created_time': 'Created Time',
        'label_created_by': 'Created By',
        'label_case_creator': 'Case Creator',
        
        # Case chat instructions
        'sync_to_support': 'Sync to AWS Support',
        'sync_instruction': '@bot [content]',
        'sync_description': ' - Sync message to AWS Support',
        'upload_attachment': 'Upload file/image',
        'upload_description': ' - Reply with "upload" to sync to AWS Support',
        'internal_discussion': 'Internal Discussion',
        'internal_discussion_1': '• Regular messages (without @bot) stay in chat only, not synced to AWS Support',
        'internal_discussion_2': '• Good for team internal discussions',
        'notification': 'Notification',
        'notification_1': '• AWS Support engineer replies will be pushed here automatically',
        'type_help': '• Type ',
        'see_more_commands': ' to see more commands',
        
        # Case creation
        'case_create_failed': '❌ Creation failed: {}',
        'case_details_title': 'AWS Support Case Details',
        
        # Card UI
        'card_header': 'Create AWS Support Case',
        'card_aws_account': 'AWS Account',
        'card_select_account': 'Select AWS Account',
        'card_case_title': 'Case Title',
        'card_aws_service': 'AWS Service',
        'card_select_service': 'Select AWS Service',
        'card_severity': 'Severity',
        'card_select_severity': 'Select Severity',
        'card_submit': 'Submit Case',
        'card_all_services': '─────── All Services ───────',
        'card_severity_low': '⚪ General guidance - 24h Response',
        'card_severity_normal': '🟡 System impaired - 12h Response',
        'card_severity_high': '🟠 Production system impaired - 4h Response',
        'card_severity_urgent': '🔴 Production system down - 1h Response',
        'card_severity_critical': '🔴 Business-critical system down - 15min Response',
        'card_issue_technical': '🔧 Technical Support',
        'card_issue_billing': '💰 Billing Issues',
        'card_issue_service': '👤 Customer Service',
        'card_assistant_title': 'AWS Support Case Assistant',
        'card_create_flow': '📝 **Create Case Flow**',
        'card_create_step1': '1. Select AWS account, service type and severity in the card',
        'card_create_step2': '2. Click "Submit Case" button',
        'card_create_step3': '3. Bot will automatically create a dedicated case chat',
        'card_communication': '💬 **Case Communication**',
        'card_comm_sync': '• In case chat **@bot [content]** syncs to AWS Support',
        'card_comm_upload': '• Send file/image, reply with "upload" to sync to case',
        'card_comm_internal': '• Regular messages are for internal discussion only',
        'card_tips': '💡 **Issue Description Tips**',
        'card_tip1': '• Time and timezone when issue occurred',
        'card_tip2': '• Resource IDs and region involved',
        'card_tip3': '• Issue symptoms and business impact',
        'card_tip4': '• Contact person and contact info',
        
        # Success messages (for original chat)
        'case_created_success': '✅ AWS Support Case Created Successfully!',
        'case_account_label': 'Account',
        'case_id_label': 'Case ID',
        'case_issue_type_label': 'Issue Type',
        'case_title_label': 'Title',
        'case_severity_label': 'Severity',
        'case_chat_created': 'A dedicated case chat has been created, updates will be notified there',
        'case_join_instruction': 'Others can join via',
        'case_join_suffix': 'to join the case chat',
        
        # Case poller messages
        'poller_message_truncated': '[Message truncated, please check AWS Console]',
        'poller_case_reply': 'Case Reply',
        'poller_case_label': 'Case',
        'poller_status_update': 'Case Status Update',
        'poller_new_status': 'New Status',
        
        # Case status
        'status_opened': '🟢 Opened',
        'status_pending_customer': '🟡 Pending Customer Action',
        'status_customer_completed': '🟢 Customer Action Completed',
        'status_reopened': '🔵 Reopened',
        'status_resolved': '✅ Resolved',
        'status_unassigned': '⚪ Unassigned',
        'status_in_progress': '🔄 In Progress',
    },
}


def get_user_language(user_id: str = None, open_id: str = None, token_func=None, message_text: str = None) -> str:
    """
    Get user's preferred language
    
    Detection priority:
    1. Command language in message_text (most reliable)
    2. User name contains Chinese characters
    3. Default to DEFAULT_LANGUAGE setting
    
    Args:
        user_id: Lark user_id
        open_id: Lark open_id
        token_func: Function to get tenant access token
        message_text: User's message text (for command language detection)
        
    Returns:
        Language code: 'zh' or 'en'
        Defaults to DEFAULT_LANGUAGE if unable to detect
    """
    import json
    import urllib3
    
    # Priority 1: Detect from command language in message
    if message_text:
        cmd_lang = detect_command_language(message_text)
        print(f"Detected language from command: {cmd_lang}, message: {message_text[:50]}")
        return cmd_lang
    
    # Priority 2: Try to detect from user name
    try:
        if not token_func:
            return DEFAULT_LANGUAGE
            
        token = token_func()
        http = urllib3.PoolManager()
        
        if open_id:
            url = f"https://open.larksuite.com/open-apis/contact/v3/users/{open_id}?user_id_type=open_id"
        elif user_id:
            url = f"https://open.larksuite.com/open-apis/contact/v3/users/{user_id}?user_id_type=user_id"
        else:
            return DEFAULT_LANGUAGE
        
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
        response = http.request('GET', url, headers=headers)
        result = json.loads(response.data.decode('utf-8'))
        
        if result.get('code') == 0:
            user_data = result.get('data', {}).get('user', {})
            name = user_data.get('name', '')
            
            # Check if name contains Chinese characters
            if any('\u4e00' <= c <= '\u9fff' for c in name):
                print(f"Detected Chinese from user name: {name}")
                return 'zh'
            else:
                print(f"No Chinese in user name: {name}, defaulting to {DEFAULT_LANGUAGE}")
                return DEFAULT_LANGUAGE
            
        print(f"Unable to get user info, defaulting to {DEFAULT_LANGUAGE}")
        return DEFAULT_LANGUAGE
        
    except Exception as e:
        print(f"Error detecting user language: {e}")
        return DEFAULT_LANGUAGE


def get_message(lang: str, key: str, *args) -> str:
    """
    Get localized message
    
    Args:
        lang: Language code ('zh' or 'en')
        key: Message key
        *args: Format arguments
        
    Returns:
        Localized message string
    """
    # Fallback to DEFAULT_LANGUAGE if language not supported
    if lang not in MESSAGES:
        lang = DEFAULT_LANGUAGE
    
    # Get message template (fallback to DEFAULT_LANGUAGE if key not found)
    template = MESSAGES[lang].get(key, MESSAGES[DEFAULT_LANGUAGE].get(key, key))
    
    # Format with arguments if provided
    if args:
        try:
            return template.format(*args)
        except:
            return template
    
    return template


def detect_command_language(text: str) -> str:
    """
    Detect which language the command is in
    
    Args:
        text: Command text
        
    Returns:
        Language code: 'zh' or 'en'
    """
    text_lower = text.lower()
    
    # Check for English commands
    if any(text_lower.startswith(cmd) for cmd in ['create case', 'reply case', 'history', 'follow', 'help']):
        return 'en'
    
    # Check for Chinese commands
    if any(text_lower.startswith(cmd) for cmd in ['开工单', '回复工单', '历史', '关注', '帮助']):
        return 'zh'
    
    # Default to DEFAULT_LANGUAGE setting
    return DEFAULT_LANGUAGE
