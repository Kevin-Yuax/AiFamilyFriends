<script setup>
import {onBeforeUnmount, ref, useTemplateRef, watch} from "vue";
import CameraIcon from "@/components/navbar/icon/CameraIcon.vue";
import Croppie from "croppie";
import 'croppie/croppie.css'

const props=defineProps(['backgroundImage'])
const myBackGroundImage=ref(props.backgroundImage)

watch( ()=> props.backgroundImage ,newVal=>{
  myBackGroundImage.value=newVal
})


const modalRef=useTemplateRef('modal-ref')
const croppieRef= useTemplateRef('croppie-ref')
let croppie= null

async function openModal(photo){
  modalRef.value.showModal()
  if (!croppie){
    croppie =new Croppie(croppieRef.value,{
      viewport: {width: 300, height: 500},
      boundary: {width: 600, height: 600},
      enableOrientation: true,
      enforceBoundary: true,
    })
  }
  croppie.bind({
    url:photo,
  })
}
async function crop(){
  if(!croppie) return
  myBackGroundImage.value = await croppie.result({  // 获取裁剪结果
    type: 'base64',
    size: 'viewport',
  })
  modalRef.value.close()
}

watch( ()=> props.photo ,newVal=>{
  myBackGroundImage.value=newVal
})

const fileInputRef=useTemplateRef('file-input-ref')

function onFileChange(e){
  const file=e.target.files[0]
  e.target.value=''
  if(!file) return

  const reader=new FileReader()
  reader.onload =()=>{
    openModal(reader.result)
  }
  reader.readAsDataURL(file)
}

onBeforeUnmount(()=>{
  croppie?.destroy()

})

defineExpose({
  myBackGroundImage,
})
</script>

<template>
  <fieldset class="fieldset">
    <label class="label">
      <span class="label-text font-medium text-gray-700 mb-2 text-[15px]">聊天背景</span>
    </label>
    <div class="avatar relative">
      <div v-if="myBackGroundImage" class="w-15 h-25">
        <img :src="myBackGroundImage",alt=" ">
      </div>
      <div v-else class="w-15 h-25 rounded-box bg-base-300"></div>
      <div @click="fileInputRef.click()" class="absolute left-0 top-0 w-15 h-25 flex justify-center items-center bg-black/20 rounded-box cursor-pointer">
        <CameraIcon/>
      </div>
    </div>

  </fieldset>

  <input ref='file-input-ref' type="file" accept="image/*" class="hidden" @change="onFileChange">

  <dialog ref="modal-ref" class="modal">
      <div class="modal-box transition-none max-w-2xl">
        <button @click="modalRef.close()" class="btn btn-circle btn-sm btn-ghost absolute right-2 top-2">✕</button>

        <div ref="croppie-ref" class="flex flex-col justify-center my-4"></div>

        <div class="modal-action flex gap-4 px-6 pb-6 justify-center">
          <button @click='modalRef.close()' class="btn btn-ghost border border-gray-200 hover:bg-gray-50 transition-all duration-200 rounded-lg w-28 py-2 text-gray-700">取消</button>
          <button @click='crop' class="btn btn-neutral hover:bg-neutral-700 text-white border-none shadow-sm hover:shadow-md transition-all duration-200 rounded-lg w-28 py-2 transform hover:-translate-y-0.5 active:translate-y-0">确定</button>
        </div>
      </div>
    </dialog>
</template>

<style scoped>

</style>