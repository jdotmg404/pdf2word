<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  type: 'success' | 'error'
  message: string
}>()

const iconPath = computed(() => {
  if (props.type === 'success') {
    return 'M20 6L9 17L4 12'
  }
  return 'M18 6L6 18M6 6L18 18'
})

const title = computed(() => {
  return props.type === 'success' ? '转换成功' : '转换失败'
})
</script>

<template>
  <div class="status-box" :class="type">
    <div class="status-icon">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path :d="iconPath" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>
    <div class="status-content">
      <p class="status-title">{{ title }}</p>
      <p class="status-message">{{ message }}</p>
    </div>
  </div>
</template>

<style scoped>
.status-box {
  display: flex;
  align-items: flex-start;
  gap: var(--spacing-md);
  padding: var(--spacing-md) var(--spacing-lg);
  border-radius: var(--radius-lg);
  animation: fadeInUp var(--transition-normal) ease forwards;
}

/* Success State */
.status-box.success {
  background: var(--color-success-light);
  border: 1px solid rgba(16, 185, 129, 0.3);
}

.status-box.success .status-icon {
  background: var(--color-success);
  color: white;
}

.status-box.success .status-title {
  color: #065f46;
}

/* Error State */
.status-box.error {
  background: var(--color-error-light);
  border: 1px solid rgba(239, 68, 68, 0.3);
}

.status-box.error .status-icon {
  background: var(--color-error);
  color: white;
}

.status-box.error .status-title {
  color: #991b1b;
}

/* Status Icon */
.status-icon {
  flex-shrink: 0;
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-full);
}

/* Status Content */
.status-content {
  flex: 1;
  min-width: 0;
}

.status-title {
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-semibold);
  margin: 0 0 var(--spacing-xs);
}

.status-message {
  font-size: var(--font-size-sm);
  color: var(--color-text-secondary);
  margin: 0;
  line-height: var(--line-height-relaxed);
}

/* Responsive */
@media (max-width: 640px) {
  .status-box {
    padding: var(--spacing-md);
  }

  .status-icon {
    width: 32px;
    height: 32px;
  }
}
</style>