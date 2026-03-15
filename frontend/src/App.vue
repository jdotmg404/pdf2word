<script setup lang="ts">
import { ref, computed } from 'vue'
import FileUpload from '@/components/FileUpload.vue'
import ProgressBar from '@/components/ProgressBar.vue'
import StatusBox from '@/components/StatusBox.vue'
import { useConverter } from '@/composables/useConverter'

const selectedFile = ref<File | null>(null)
const fileName = computed(() => selectedFile.value?.name || '')
const fileSize = computed(() => {
  if (!selectedFile.value) return ''
  const bytes = selectedFile.value.size
  if (bytes < 1024) return bytes + ' B'
  if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB'
  return (bytes / (1024 * 1024)).toFixed(2) + ' MB'
})

const {
  progress,
  message,
  stage,
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
    return '转换完成！文件已开始下载，请选择保存位置'
  }
  return errorMessage.value || '转换失败，请重试'
})

const handleFileSelect = (file: File) => {
  selectedFile.value = file
}

const handleFileClear = () => {
  selectedFile.value = null
}

const handleConvert = async () => {
  if (!selectedFile.value) {
    return
  }
  await startConversion(selectedFile.value)
}
</script>

<template>
  <div class="app-container">
    <!-- Brand Section -->
    <header class="brand-section">
      <div class="brand-icon">
        <svg width="40" height="40" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M14 2H6C5.46957 2 4.96086 2.21071 4.58579 2.58579C4.21071 2.96086 4 3.46957 4 4V20C4 20.5304 4.21071 21.0391 4.58579 21.4142C4.96086 21.7893 5.46957 22 6 22H18C18.5304 22 19.0391 21.7893 19.4142 21.4142C19.7893 21.0391 20 20.5304 20 20V8L14 2Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M14 2V8H20" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M16 13H8" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M16 17H8" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M10 9H9H8" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
      <h1 class="brand-title">PDF to Word</h1>
      <p class="brand-subtitle">快速、安全、免费转换</p>
    </header>

    <!-- Main Card -->
    <main class="main-card glass-card">
      <!-- Upload Section -->
      <section class="upload-section">
        <FileUpload
          :disabled="isConverting"
          :file-name="fileName"
          :file-size="fileSize"
          @select="handleFileSelect"
          @clear="handleFileClear"
        />
      </section>

      <!-- Action Section -->
      <section class="action-section">
        <button
          :disabled="isConverting || !selectedFile"
          class="convert-btn"
          @click="handleConvert"
        >
          <span v-if="isConverting" class="btn-loading">
            <span class="spinner"></span>
            转换中...
          </span>
          <span v-else class="btn-content">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M13 2L3 14H12L11 22L21 10H12L13 2Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            开始转换
          </span>
        </button>
      </section>

      <!-- Progress Section -->
      <section v-if="showProgress" class="progress-section">
        <ProgressBar
          :percent="progress"
          :message="message"
          :stage="stage"
          :is-complete="status === 'success'"
        />
      </section>

      <!-- Status Section -->
      <section v-if="showStatus" class="status-section">
        <StatusBox
          :type="statusType"
          :message="statusMessage"
        />
      </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
      <p>支持标准 PDF 格式 · 转换后自动下载</p>
    </footer>
  </div>
</template>

<style scoped>
.app-container {
  width: 100%;
  max-width: var(--container-max-width);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--spacing-lg);
}

/* Brand Section */
.brand-section {
  text-align: center;
  animation: fadeInDown var(--transition-slow) ease forwards;
}

.brand-icon {
  width: 64px;
  height: 64px;
  margin: 0 auto var(--spacing-md);
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-radius: var(--radius-xl);
  color: white;
}

.brand-title {
  font-size: var(--font-size-2xl);
  font-weight: var(--font-weight-bold);
  color: white;
  margin-bottom: var(--spacing-xs);
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.brand-subtitle {
  font-size: var(--font-size-sm);
  color: rgba(255, 255, 255, 0.8);
  margin: 0;
}

/* Main Card */
.main-card {
  width: 100%;
  padding: var(--spacing-xl);
  animation: scaleIn var(--transition-slow) ease forwards;
}

/* Upload Section */
.upload-section {
  margin-bottom: var(--spacing-lg);
}

/* Action Section */
.action-section {
  display: flex;
  justify-content: center;
  margin-bottom: var(--spacing-lg);
}

.convert-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--spacing-sm);
  padding: var(--spacing-md) var(--spacing-2xl);
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-semibold);
  color: white;
  background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-primary-end) 100%);
  border: none;
  border-radius: var(--radius-xl);
  cursor: pointer;
  transition: all var(--transition-normal);
  box-shadow: var(--shadow-glow);
  min-width: 180px;
}

.convert-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 30px rgba(139, 92, 246, 0.5);
}

.convert-btn:active:not(:disabled) {
  transform: translateY(0);
}

.convert-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

.btn-content,
.btn-loading {
  display: inline-flex;
  align-items: center;
  gap: var(--spacing-sm);
}

.spinner {
  width: 18px;
  height: 18px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

/* Progress Section */
.progress-section {
  margin-bottom: var(--spacing-lg);
}

/* Status Section */
.status-section {
  animation: fadeInUp var(--transition-normal) ease forwards;
}

/* Footer */
.footer {
  text-align: center;
  color: rgba(255, 255, 255, 0.7);
  font-size: var(--font-size-sm);
  animation: fadeIn var(--transition-slow) ease forwards;
}

.footer p {
  margin: 0;
}

/* Responsive */
@media (max-width: 640px) {
  .app-container {
    padding: var(--spacing-md);
  }

  .main-card {
    padding: var(--spacing-lg);
  }

  .brand-title {
    font-size: var(--font-size-xl);
  }

  .convert-btn {
    width: 100%;
    min-width: auto;
  }
}
</style>