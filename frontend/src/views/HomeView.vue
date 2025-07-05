<!-- HomeView.vue -->
<script setup lang="ts">
import { ref } from 'vue'
import PLI5Button from '../components/PLI5Button.vue'
import PDFViewer from '../components/PDFViewer.vue'
import HomeService from '../services/HomeService'
const userUploadedPDF = ref<File | null>(null)
const privacySimplifiedPDF = ref<File | null>(null)
function handleFile(event: Event) {
  const target = event.target as HTMLInputElement
  const file = target.files?.[0]
  userUploadedPDF.value = file ?? null
}
async function handleArrow() {
  if (!userUploadedPDF.value) {
    console.error('No file selected to simplify.')
    return
  }

  try {
    const response = await HomeService.simplifyPDF(userUploadedPDF.value)
    const file = new File([response.data], 'simplified_policy.pdf', {
      type: 'application/pdf',
    })
    privacySimplifiedPDF.value = file
  } catch (error) {
    console.error('Failed to simplify PDF:', error)
  }
}
</script>

<template>
  <div class="container min-h-screen items-center flex mx-auto bg-gray-100">
    <div class="basis-2/5 min-w-0">
      <label
        class="inline-block bg-blue-500 text-white px-4 py-2 rounded cursor-pointer hover:bg-blue-600 transition-colors"
        for="fileInput"
      >
        Choose File
      </label>
      <input
        id="fileInput"
        type="file"
        accept="application/pdf"
        class="hidden"
        @change="handleFile"
      />
      <PDFViewer :pdf-source="userUploadedPDF"></PDFViewer>
    </div>
    <PLI5Button @arrow-pressed="handleArrow" class="basis-1/5 flex-shrink-0"></PLI5Button>
    <PDFViewer :pdf-source="privacySimplifiedPDF" class="basis-2/5 min-w-0"></PDFViewer>
  </div>
</template>
