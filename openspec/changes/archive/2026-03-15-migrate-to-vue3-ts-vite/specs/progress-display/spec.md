## ADDED Requirements

### Requirement: 实时进度显示
系统 SHALL 通过 SSE 接收并显示转换进度。

#### Scenario: 显示转换进度
- **WHEN** 后端发送 progress 事件
- **THEN** 进度条更新到对应的百分比，并显示进度消息

#### Scenario: 进度从 0 到 100
- **WHEN** 转换进行中
- **THEN** 进度条从 0% 逐步更新到 100%

### Requirement: 转换完成提示
系统 SHALL 在转换完成时显示成功状态。

#### Scenario: 转换成功
- **WHEN** 后端发送 complete 事件
- **THEN** 进度条显示 100%，显示"转换完成！"消息

### Requirement: 错误处理
系统 SHALL 显示转换失败的错误信息。

#### Scenario: 转换失败
- **WHEN** 后端发送 error 事件或网络错误
- **THEN** 显示错误消息，进度条重置

### Requirement: 状态消息显示
系统 SHALL 使用状态框显示操作结果。

#### Scenario: 成功状态显示
- **WHEN** 转换成功完成
- **THEN** 状态框显示绿色背景的成功消息

#### Scenario: 错误状态显示
- **WHEN** 转换失败
- **THEN** 状态框显示红色背景的错误消息