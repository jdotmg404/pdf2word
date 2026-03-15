import { ref, type Ref } from 'vue'
import type { CompleteEvent, ConversionStatus } from '@/types/api'

const API_BASE = ''

interface UseConverter {
  progress: Ref<number>
  message: Ref<string>
  status: Ref<ConversionStatus>
  errorMessage: Ref<string>
  startConversion: (file: File) => Promise<void>
  reset: () => void
}

export function useConverter(): UseConverter {
  const progress = ref(0)
  const message = ref('')
  const status = ref<ConversionStatus>('idle')
  const errorMessage = ref('')

  const reset = () => {
    progress.value = 0
    message.value = ''
    status.value = 'idle'
    errorMessage.value = ''
  }

  const startConversion = async (file: File) => {
    reset()
    status.value = 'converting'
    message.value = '准备转换...'

    const formData = new FormData()
    formData.append('file', file)

    try {
      const response = await fetch(`${API_BASE}/convert-stream`, {
        method: 'POST',
        body: formData,
      })

      if (!response.ok) {
        throw new Error('服务器响应错误')
      }

      const reader = response.body?.getReader()
      if (!reader) {
        throw new Error('无法读取响应流')
      }

      const decoder = new TextDecoder()
      let buffer = ''

      while (true) {
        const { done, value } = await reader.read()
        if (done) break

        buffer += decoder.decode(value, { stream: true })

        // 解析 SSE 事件
        const lines = buffer.split('\n')
        buffer = lines.pop() || ''

        let eventType = 'message'
        for (const line of lines) {
          if (line.startsWith('event: ')) {
            eventType = line.substring(7).trim()
          } else if (line.startsWith('data: ')) {
            const data = JSON.parse(line.substring(6))

            if (eventType === 'progress') {
              progress.value = data.percent
              message.value = `${data.message} (${data.percent}%)`
            } else if (eventType === 'complete') {
              handleComplete(data)
              return
            } else if (eventType === 'error') {
              throw new Error(data.error || '转换失败')
            }
          }
        }
      }
    } catch (err) {
      status.value = 'error'
      errorMessage.value = err instanceof Error ? err.message : '未知错误'
      progress.value = 0
    }
  }

  const handleComplete = (data: CompleteEvent) => {
    progress.value = 100
    message.value = '转换完成！正在下载...'
    status.value = 'success'

    // 触发下载
    const downloadUrl = `${API_BASE}/download/${data.download_id}`
    const a = document.createElement('a')
    a.href = downloadUrl
    a.download = data.filename
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)

    message.value = '转换完成！文件已开始下载，请选择保存位置'
  }

  return {
    progress,
    message,
    status,
    errorMessage,
    startConversion,
    reset,
  }
}