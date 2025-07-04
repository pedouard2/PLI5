<script setup lang="ts">
import ArrowIcon from '../assets/arrow-right.svg'
const emit = defineEmits(['arrow-pressed'])

const handleSubmit = () => {
  emit('arrow-pressed')
}
</script>

<template>
  <div
    class="w-full h-full flex items-center justify-center border-2 rounded-r-lg border-dashed border-gray-300"
  >
    <button
      @click="handleSubmit"
      class="p-2 flex items-center justify-center rounded-lg hover:bg-gray-100"
    >
      <ArrowIcon class="cursor-pointer fill-blue-500 w-[50%] h-[50%]" />
    </button>
  </div>
</template>
