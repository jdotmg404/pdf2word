<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  percent: number
  message: string
  stage?: string
  isComplete?: boolean
}>()

const progressWidth = computed(() => `${Math.min(100, Math.max(0, props.percent))}%`)

const stageLabels: Record<string, string> = {
  parsing: '解析 PDF',
  extracting: '提取内容',
  converting: '生成 Word',
  finalizing: '完成处理'
}

const displayStage = computed(() => {
  if (props.stage && stageLabels[props.stage]) {
    return stageLabels[props.stage]
  }
  return null
})
</script>

<template>
  <div class="progress-container" :class="{ 'is-complete': isComplete }">
    <!-- Progress Header -->
    <div class="progress-header">
      <span class="progress-percent">{{ Math.round(percent) }}%</span>
      <span v-if="displayStage" class="progress-stage">{{ displayStage }}</span>
    </div>

    <!-- Progress Bar -->
    <div class="progress-bar">
      <div
        class="progress-fill"
        :style="{ width: progressWidth }"
      >
        <div class="progress-shimmer"></div>
      </div>
    </div>

    <!-- Progress Message -->
    <p class="progress-message">{{ message }}</p>
  </div>
</template>

<style scoped>
.progress-container {
  width: 100%;
}

/* Progress Header */
.progress-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: var(--spacing-sm);
}

.progress-percent {
  font-size: var(--font-size-2xl);
  font-weight: var(--font-weight-bold);
  background: linear-gradient(135deg, var(--color-primary), var(--color-primary-end));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.progress-stage {
  font-size: var(--font-size-sm);
  color: var(--color-text-secondary);
  background: var(--color-gray-100);
  padding: var(--spacing-xs) var(--spacing-sm);
  border-radius: var(--radius-md);
}

/* Progress Bar */
.progress-bar {
  width: 100%;
  height: 12px;
  background: var(--color-gray-100);
  border-radius: var(--radius-full);
  overflow: hidden;
  position: relative;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--color-primary) 0%, var(--color-primary-end) 100%);
  border-radius: var(--radius-full);
  transition: width var(--transition-normal) ease-out;
  position: relative;
  overflow: hidden;
}

/* Shimmer Effect */
.progress-shimmer {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(
    90deg,
    transparent 0%,
    rgba(255, 255, 255, 0.4) 50%,
    transparent 100%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}

/* Complete State */
.progress-container.is-complete .progress-fill {
  background: linear-gradient(90deg, var(--color-success) 0%, #34d399 100%);
}

.progress-container.is-complete .progress-shimmer {
  animation: none;
  background: transparent;
}

.progress-container.is-complete .progress-percent {
  background: linear-gradient(135deg, var(--color-success), #34d399);
  -webkit-background-clip: text;
  background-clip: text;
}

/* Progress Message */
.progress-message {
  margin-top: var(--spacing-sm);
  font-size: var(--font-size-sm);
  color: var(--color-text-secondary);
  text-align: center;
}

/* Responsive */
@media (max-width: 640px) {
  .progress-percent {
    font-size: var(--font-size-xl);
  }

  .progress-bar {
    height: 10px;
  }
}
</style>