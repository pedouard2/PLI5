<!-- App.vue -->
<script setup lang="ts">
import { ref } from "vue";
import FileUploader from "./components/FileUploader.vue";
const selectedFile = ref<File | null>(null);
const fileContent = ref<string>("HIIII");

async function handleFile(file: File | undefined) {
  console.log(file);
  selectedFile.value = file ?? null;
  // if (file) {
  //   fileContent.value = await file.text();
  // }
}
</script>

<template>
  <div class="container min-h-screen items-center flex mx-auto bg-gray-100">
    <FileUploader @file-selected="handleFile" class="basis-2/5"></FileUploader>
    <div class="px-4 rounded-lg basis-1/5 border-2 border-dashed">Arrow</div>
    <div
      v-if="fileContent"
      class="px-4 overflow-y-auto max-h-96 whitespace-pre-wrap rounded-lg basis-2/5 border-2 border-dashed"
    >
      {{ fileContent }}
    </div>
  </div>
</template>
