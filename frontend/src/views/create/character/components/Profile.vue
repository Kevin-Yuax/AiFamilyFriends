<script setup>
import {ref, watch} from "vue";

const props=defineProps(['profile'])
const myProfile=ref(props.profile)

watch( ()=> props.profile ,newVal=>{
  myProfile.value=newVal
})

defineExpose({
  myProfile,
})
</script>

<template>
  <div class="form-control w-full">
    <label class="label">
      <span class="label-text font-medium text-gray-700 mb-1 text-[15px]">角色介绍</span>
    </label>
    <textarea
      v-model="myProfile"
      rows="5"
      class="textarea textarea-bordered w-full rounded-xl border-gray-200 bg-white/80 backdrop-blur-sm focus:border-indigo-300 focus:ring-2 focus:ring-indigo-200 transition-all resize-none shadow-sm
text-[14px]"
      placeholder="介绍一下角色吧..."
    ></textarea>

  </div>
</template>

<style scoped>

</style>