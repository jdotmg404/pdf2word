<script setup lang="ts">
defineProps<{
  disabled?: boolean
  fileName?: string
}>()

const emit = defineEmits<{
  (e: 'select', file: File): void
}>()

const handleFileChange = (event: Event) => {
  const target = event.target as HTMLInputElement
  const file = target.files?.[0]
  if (file) {
    emit('select', file)
  }
}
</script>

<template>
  <div class="file-upload">
    <input
      type="file"
      accept=".pdf"
      :disabled="disabled"
      @change="handleFileChange"
    />
    <p v-if="fileName" class="file-name">已选择: {{ fileName }}</p>
  </div>
</template>

<style scoped>
.file-upload input[type="file"] {
  cursor: pointer;
}

.file-name {
  margin-top: 8px;
  color: #666;
  font-size: 14px;
}
</style>