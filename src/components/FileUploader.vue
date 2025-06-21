<script setup lang="ts">
import { ref, onUnmounted } from "vue";
import { VuePDF, usePDF } from "@tato30/vue-pdf";

const emit = defineEmits(["file-selected"]);

const pdfSource = ref<string | null>(null);
const fileName = ref<string>("");

const { pdf, error, pages } = usePDF(pdfSource);

const handleFileChange = (event: Event) => {
  const target = event.target as HTMLInputElement;
  const file = target.files?.[0];

  emit("file-selected", file);
  fileName.value = file?.name ?? "";

  if (pdfSource.value) {
    URL.revokeObjectURL(pdfSource.value);
  }

  if (file && file.type === "application/pdf") {
    pdfSource.value = URL.createObjectURL(file);
  } else {
    pdfSource.value = null;
  }
};

onUnmounted(() => {
  if (pdfSource.value) {
    URL.revokeObjectURL(pdfSource.value);
  }
});
</script>

<template>
  <div
    class="px-4 py-8 flex flex-col items-center gap-4 rounded-lg border-2 border-dashed border-gray-300"
  >
    <p v-if="fileName" class="text-sm text-gray-600">{{ fileName }}</p>

    <label
      class="inline-block bg-blue-500 text-white px-4 py-2 rounded cursor-pointer hover:bg-blue-600 transition-colors"
      for="file_input"
    >
      Choose File
    </label>
    <input
      id="file_input"
      type="file"
      class="hidden"
      @change="handleFileChange"
    />

    <div class="w-full mt-4">
      <div
        v-if="error"
        class="text-center p-4 bg-red-100 text-red-700 rounded-lg"
      >
        <p>Error loading PDF:</p>
        <p class="text-sm">{{ (error as Error).message }}</p>
      </div>

      <div
        v-else-if="pdf"
        class="max-h-[70vh] overflow-y-auto border border-gray-200 rounded-lg bg-gray-50"
      >
        <div v-for="page in pages" :key="page" class="flex justify-center my-4">
          <VuePDF :pdf="pdf" :page="page" :scale="1.5" />
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
