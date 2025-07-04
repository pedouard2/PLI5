<!-- PDFViewer -->
<script setup lang="ts">
import { ref, watch, onUnmounted, PropType } from 'vue'
import { VuePDF, usePDF } from '@tato30/vue-pdf'

const props = defineProps({
  pdfSource: {
    type: [File, null] as PropType<File | null>,
    default: null,
  },
})

const sourceUrl = ref<string | null>(null)
const fileName = ref<string>('')

const { pdf, pages } = usePDF(sourceUrl)

watch(
  () => props.pdfSource,
  (newSource) => {
    if (sourceUrl.value) {
      URL.revokeObjectURL(sourceUrl.value)
    }

    if (newSource && newSource.type === 'application/pdf') {
      sourceUrl.value = URL.createObjectURL(newSource)
      fileName.value = newSource.name
    } else {
      sourceUrl.value = null
      fileName.value = newSource ? newSource.name : ''
    }
  },
  { immediate: true }
)

onUnmounted(() => {
  if (sourceUrl.value) {
    URL.revokeObjectURL(sourceUrl.value)
  }
})
</script>

<template>
  <div
    class="px-4 py-8 flex flex-col items-center gap-4 rounded-lg border-2 border-dashed border-gray-300"
  >
    <h3 v-if="fileName" class="text-sm text-gray-600">{{ fileName }}</h3>

    <div class="w-full mt-4">
      <!-- <div v-if="error" class="text-center p-4 bg-red-100 text-red-700 rounded-lg">
        <p>Error loading PDF:</p>
        <p class="text-sm">{{ (error as Error).message }}</p>
      </div> -->

      <div
        v-if="pdf"
        class="max-h-[70vh] overflow-y-auto border border-gray-200 rounded-lg bg-gray-50"
      >
        <div v-for="page in pages" :key="page" class="flex justify-center my-4">
          <VuePDF :pdf="pdf" :page="page" :scale="1.0" />
        </div>
      </div>

      <div
        v-else-if="fileName && !pdfSource"
        class="text-center p-4 bg-yellow-100 text-yellow-700 rounded-lg"
      >
        <p>Preview is only available for PDF files.</p>
      </div>
    </div>
  </div>
</template>
