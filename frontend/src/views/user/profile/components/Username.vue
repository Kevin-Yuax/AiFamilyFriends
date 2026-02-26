<script setup>
import { ref, watch } from "vue";

const props = defineProps(['username']);
const myUsername = ref(props.username);

watch(() => props.username, (newVal) => {
  myUsername.value = newVal;
});
defineExpose({
  myUsername,
})
</script>

<template>
  <fieldset class="fieldset">
    <label class="label">
      <span class="label-text font-medium text-gray-700 mb-2 text-[15px]">用户名</span>
    </label>
    <input
      v-model="myUsername"
      type="text"
      class="input input-bordered w-full rounded-xl border-gray-200 bg-white/80 backdrop-blur-sm focus:border-indigo-300 focus:ring-2 focus:ring-indigo-200 transition-all shadow-sm
text-[14px]"
      placeholder="请输入用户名"
    />

  </fieldset>
</template>

<style scoped>
/* 如有需要，可在此添加额外样式 */
</style>