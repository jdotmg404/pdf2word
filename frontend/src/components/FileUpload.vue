<script setup lang="ts">
import { ref, computed } from 'vue'

const props = defineProps<{
  disabled?: boolean
  fileName?: string
  fileSize?: string
}>()

const emit = defineEmits<{
  (e: 'select', file: File): void
  (e: 'clear'): void
}>()

const isDragOver = ref(false)
const inputRef = ref<HTMLInputElement | null>(null)
const errorMessage = ref('')

const hasFile = computed(() => !!props.fileName)

const handleDragOver = (event: DragEvent) => {
  if (props.disabled) return
  event.preventDefault()
  event.stopPropagation()
  isDragOver.value = true
}

const handleDragLeave = (event: DragEvent) => {
  event.preventDefault()
  event.stopPropagation()
  isDragOver.value = false
}

const handleDrop = (event: DragEvent) => {
  event.preventDefault()
  event.stopPropagation()
  isDragOver.value = false

  if (props.disabled) return

  const files = event.dataTransfer?.files
  if (files && files.length > 0) {
    validateAndSelect(files[0])
  }
}

const handleFileChange = (event: Event) => {
  const target = event.target as HTMLInputElement
  const files = target.files
  if (files && files.length > 0) {
    validateAndSelect(files[0])
  }
  // Reset input so the same file can be selected again
  target.value = ''
}

const validateAndSelect = (file: File) => {
  errorMessage.value = ''

  // Check file type
  if (file.type !== 'application/pdf') {
    errorMessage.value = '仅支持 PDF 文件格式'
    return
  }

  emit('select', file)
}

const handleClear = () => {
  errorMessage.value = ''
  emit('clear')
}
</script>

<template>
  <div class="file-upload">
    <!-- Drop Zone -->
    <div
      v-if="!hasFile"
      class="drop-zone"
      :class="{
        'is-drag-over': isDragOver,
        'is-disabled': disabled
      }"
      @dragover="handleDragOver"
      @dragleave="handleDragLeave"
      @drop="handleDrop"
    >
      <input
        ref="inputRef"
        type="file"
        accept=".pdf,application/pdf"
        :disabled="disabled"
        @change="handleFileChange"
      />

      <div class="drop-zone-content">
        <div class="upload-icon">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M21 15V19C21 19.5304 20.7893 20.0391 20.4142 20.4142C20.0391 20.7893 19.5304 21 19 21H5C4.46957 21 3.96086 20.7893 3.58579 20.4142C3.21071 20.0391 3 19.5304 3 19V15" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M17 8L12 3L7 8" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M12 3V15" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <p class="drop-text-main">拖拽文件到此处</p>
        <p class="drop-text-sub">或点击选择文件</p>
        <p class="drop-text-hint">支持 .pdf 格式</p>
      </div>
    </div>

    <!-- File Preview -->
    <div v-else class="file-preview" :class="{ 'is-disabled': disabled }">
      <div class="file-icon">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M14 2H6C5.46957 2 4.96086 2.21071 4.58579 2.58579C4.21071 2.96086 4 3.46957 4 4V20C4 20.5304 4.21071 21.0391 4.58579 21.4142C4.96086 21.7893 5.46957 22 6 22H18C18.5304 22 19.0391 21.7893 19.4142 21.4142C19.7893 21.0391 20 20.5304 20 20V8L14 2Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M14 2V8H20" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
      <div class="file-info">
        <p class="file-name">{{ fileName }}</p>
        <p class="file-size">{{ fileSize }}</p>
      </div>
      <button
        v-if="!disabled"
        class="clear-btn"
        @click.stop="handleClear"
        title="移除文件"
      >
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M18 6L6 18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M6 6L18 18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
    </div>

    <!-- Error Message -->
    <p v-if="errorMessage" class="error-message">
      {{ errorMessage }}
    </p>
  </div>
</template>

<style scoped>
.file-upload {
  width: 100%;
}

/* Drop Zone */
.drop-zone {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: var(--spacing-2xl) var(--spacing-lg);
  border: 2px dashed var(--color-gray-300);
  border-radius: var(--radius-xl);
  background: rgba(255, 255, 255, 0.5);
  cursor: pointer;
  transition: all var(--transition-normal);
}

.drop-zone:hover:not(.is-disabled) {
  border-color: var(--color-primary);
  background: rgba(139, 92, 246, 0.05);
}

.drop-zone.is-drag-over {
  border-color: var(--color-primary);
  border-style: solid;
  background: rgba(139, 92, 246, 0.1);
  transform: scale(1.02);
}

.drop-zone.is-disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.drop-zone input[type="file"] {
  position: absolute;
  width: 100%;
  height: 100%;
  opacity: 0;
  cursor: pointer;
}

.drop-zone.is-disabled input[type="file"] {
  pointer-events: none;
}

.drop-zone-content {
  text-align: center;
  pointer-events: none;
}

.upload-icon {
  color: var(--color-primary);
  margin-bottom: var(--spacing-md);
  transition: transform var(--transition-normal);
}

.drop-zone:hover:not(.is-disabled) .upload-icon {
  transform: translateY(-4px);
}

.drop-text-main {
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-primary);
  margin: 0 0 var(--spacing-xs);
}

.drop-text-sub {
  font-size: var(--font-size-sm);
  color: var(--color-text-secondary);
  margin: 0 0 var(--spacing-sm);
}

.drop-text-hint {
  font-size: var(--font-size-xs);
  color: var(--color-text-muted);
  margin: 0;
}

/* File Preview */
.file-preview {
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
  padding: var(--spacing-md) var(--spacing-lg);
  background: rgba(255, 255, 255, 0.8);
  border: 1px solid var(--color-gray-200);
  border-radius: var(--radius-lg);
  transition: all var(--transition-normal);
}

.file-preview.is-disabled {
  opacity: 0.6;
}

.file-icon {
  flex-shrink: 0;
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, var(--color-primary-start), var(--color-primary-end));
  border-radius: var(--radius-md);
  color: white;
}

.file-info {
  flex: 1;
  min-width: 0;
}

.file-name {
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-primary);
  margin: 0 0 var(--spacing-xs);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.file-size {
  font-size: var(--font-size-sm);
  color: var(--color-text-muted);
  margin: 0;
}

.clear-btn {
  flex-shrink: 0;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: transparent;
  border: none;
  border-radius: var(--radius-md);
  color: var(--color-text-muted);
  cursor: pointer;
  transition: all var(--transition-fast);
}

.clear-btn:hover {
  background: var(--color-error-light);
  color: var(--color-error);
}

/* Error Message */
.error-message {
  margin-top: var(--spacing-sm);
  padding: var(--spacing-sm) var(--spacing-md);
  font-size: var(--font-size-sm);
  color: var(--color-error);
  background: var(--color-error-light);
  border-radius: var(--radius-md);
}

/* Responsive */
@media (max-width: 640px) {
  .drop-zone {
    padding: var(--spacing-xl) var(--spacing-md);
  }

  .file-preview {
    padding: var(--spacing-md);
  }
}
</style>