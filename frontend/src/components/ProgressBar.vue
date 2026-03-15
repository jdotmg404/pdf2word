<script setup lang="ts">
defineProps<{
  percent: number
  message: string
  visible: boolean
}>()
</script>

<template>
  <div v-if="visible" class="progress-container">
    <div class="progress-bar">
      <div class="progress-inner" :style="{ width: `${percent}%` }"></div>
    </div>
    <p class="progress-text">{{ message }}</p>
  </div>
</template>

<style scoped>
.progress-container {
  margin-top: 10px;
}

.progress-bar {
  width: 100%;
  height: 10px;
  background: #eee;
  border-radius: 5px;
  overflow: hidden;
}

.progress-inner {
  height: 100%;
  background: #4caf50;
  transition: width 0.3s ease;
}

.progress-text {
  margin-top: 8px;
  color: #666;
  font-size: 14px;
}
</style>