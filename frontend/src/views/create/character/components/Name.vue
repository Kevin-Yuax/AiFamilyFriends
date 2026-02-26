<script setup>
import {ref, watch} from "vue";

const props=defineProps(['name'])
const myName=ref(props.name)

watch( ()=> props.name ,newVal=>{
  myName.value=newVal
})

defineExpose({
  myName,
})
</script>

<template>
  <fieldset class="fieldset">
    <label class="label">
      <span class="label-text font-medium text-gray-700 mb-2 text-[15px]">角色名</span>
    </label>
    <input
      v-model="myName"
      type="text"
      class="input input-bordered w-full rounded-xl border-gray-200 bg-white/80 backdrop-blur-sm focus:border-indigo-300 focus:ring-2 focus:ring-indigo-200 transition-all shadow-sm
text-[14px]"
      placeholder="请输入角色名"
    />

  </fieldset>
</template>

<style scoped>

</style>