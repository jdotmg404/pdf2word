// SSE 事件类型定义

export interface ProgressEvent {
  percent: number
  message: string
}

export interface CompleteEvent {
  download_id: string
  filename: string
}

export interface ErrorEvent {
  error: string
}

// SSE 事件联合类型
export type SSEEvent =
  | { type: 'progress'; data: ProgressEvent }
  | { type: 'complete'; data: CompleteEvent }
  | { type: 'error'; data: ErrorEvent }

// 转换状态
export type ConversionStatus = 'idle' | 'converting' | 'success' | 'error'