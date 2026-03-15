<script setup lang="ts">
import { ref, computed } from 'vue'
import FileUpload from '@/components/FileUpload.vue'
import ProgressBar from '@/components/ProgressBar.vue'
import StatusBox from '@/components/StatusBox.vue'
import { useConverter } from '@/composables/useConverter'

const selectedFile = ref<File | null>(null)
const fileName = computed(() => selectedFile.value?.name || '')

const {
  progress,
  message,
  status,
  errorMessage,
  startConversion,
} = useConverter()

const isConverting = computed(() => status.value === 'converting')
const showProgress = computed(() => status.value === 'converting' || status.value === 'success')
const showStatus = computed(() => status.value === 'success' || status.value === 'error')
const statusType = computed(() => status.value === 'success' ? 'success' : 'error')
const statusMessage = computed(() => {
  if (status.value === 'success') {
    return '<strong>转换完成！</strong><br>文件已开始下载，请选择保存位置'
  }
  return '错误: ' + errorMessage.value
})

const handleFileSelect = (file: File) => {
  selectedFile.value = file
}

const handleConvert = async () => {
  if (!selectedFile.value) {
    alert('请先选择一个 PDF 文件')
    return
  }
  await startConversion(selectedFile.value)
}
</script>

<template>
  <div class="container">
    <h2>PDF 转 Word</h2>
    <p>选择电脑中的 PDF 文件进行转换：</p>

    <FileUpload
      :disabled="isConverting"
      :file-name="fileName"
      @select="handleFileSelect"
    />

    <button
      :disabled="isConverting"
      class="convert-btn"
      @click="handleConvert"
    >
      开始转换
    </button>

    <ProgressBar
      :percent="progress"
      :message="message"
      :visible="showProgress"
    />

    <StatusBox
      :type="statusType"
      :message="statusMessage"
      :visible="showStatus"
    />
  </div>
</template>

<style>
body {
  font-family: sans-serif;
  padding: 50px;
  line-height: 1.6;
}

.container {
  max-width: 500px;
  margin: auto;
  border: 1px solid #ddd;
  padding: 20px;
  border-radius: 8px;
}

.convert-btn {
  margin-top: 10px;
  cursor: pointer;
}

.convert-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>