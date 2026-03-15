<script setup lang="ts">
defineProps<{
  type: 'success' | 'error'
  message: string
  visible: boolean
}>()
</script>

<template>
  <div
    v-if="visible"
    class="status-box"
    :class="type"
    v-html="message"
  ></div>
</template>

<style scoped>
.status-box {
  margin-top: 20px;
  padding: 10px;
  border-radius: 4px;
  font-size: 14px;
}

.status-box.success {
  background: #e8f5e9;
  color: #2e7d32;
}

.status-box.error {
  background: #ffebee;
  color: #c62828;
}
</style>