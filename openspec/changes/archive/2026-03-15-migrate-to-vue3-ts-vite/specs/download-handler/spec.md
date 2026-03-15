## ADDED Requirements

### Requirement: 自动下载
系统 SHALL 在转换完成后自动触发文件下载。

#### Scenario: 自动下载转换结果
- **WHEN** 后端发送 complete 事件包含 download_id 和 filename
- **THEN** 系统自动创建下载链接并触发下载

### Requirement: 下载 URL 构建
系统 SHALL 正确构建下载 URL。

#### Scenario: 下载 URL 格式
- **WHEN** 收到 complete 事件
- **THEN** 下载 URL 为 `{BASE_URL}/download/{download_id}`，文件名为 `filename`

### Requirement: 下载完成提示
系统 SHALL 在下载开始后显示完成提示。

#### Scenario: 下载提示
- **WHEN** 文件下载开始
- **THEN** 显示"转换完成！文件已开始下载，请选择保存位置"消息