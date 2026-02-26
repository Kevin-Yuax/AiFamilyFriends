<script setup>

import Photo from "@/views/create/character/components/Photo.vue";
import Profile from "@/views/create/character/components/Profile.vue";
import BackgroundImage from "@/views/create/character/components/BackgroundImage.vue";
import Name from "@/views/create/character/components/Name.vue";
import {ref, useTemplateRef} from "vue";
import {base64ToFile} from "@/js/utils/base_64-file.js";
import api from "@/js/http/api.js";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user.js";

const user=useUserStore()
const router=useRouter()

const photoRef=useTemplateRef('photo-ref')
const nameRef=useTemplateRef('name-ref')
const profileRef=useTemplateRef('profile-ref')
const backgroundImageRef=useTemplateRef('background-image-ref')
const errorMessage=ref('')

async function handleCreate(){
  const photo=photoRef.value.myPhoto
  const name=nameRef.value.myName?.trim()
  const profile=profileRef.value.myProfile?.trim()
  const backgroundImage=backgroundImageRef.value.myBackGroundImage
  errorMessage.value=''
  if (!photo){
    errorMessage.value='头像不能为空'
  }else if (!name){
    errorMessage.value='名称不能为空'
  }else if (!profile){
    errorMessage.value='角色介绍不能为空'
  }else if (!backgroundImage){
    errorMessage.value='聊天背景不能为空'
  }else {
    const formData=new FormData()
    formData.append('name', name)
    formData.append('profile',profile)
    formData.append('photo',base64ToFile(photo,'photo.png'))
    formData.append('background_image',base64ToFile(backgroundImage,'background_image.png'))
    for (let [key, value] of formData.entries()) {
      console.log(key, value);
    }
    try{
      const res=await api.post('/api/create/character/create/',formData)
      const data=res.data
      if (data.result === 'success'){
        console.log('后端返回数据：', data);
        await router.push({
          name:'user-space-index',
          params:{
            user_id:user.id,
          }
        })

      }else {
        errorMessage.value= data.result
      }
    }catch (err){
      console.log(err)
    }
  }


}

</script>

<template>
  <div class="flex justify-center">
    <div class="card bg-white/90 backdrop-blur-sm shadow-xl w-full max-w-lg border border-gray-200/60 transition-all hover:shadow-2xl mt-16">
      <div class="card-body p-6 md:p-8">
        <div class="mb-6">
          <h2 class="text-2xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">
            创建角色
          </h2>
          <div class="w-16 h-1 bg-gradient-to-r from-indigo-500 to-purple-500 rounded-full mt-2"></div>
        </div>
        <Photo ref="photo-ref"/>
        <Name ref="name-ref"/>
        <Profile ref="profile-ref"/>
        <BackgroundImage ref="background-image-ref"/>

        <p v-if="errorMessage" class="text-sm text-red-500">{{errorMessage}}</p>

        <div class="card-actions justify-center mt-8">
          <button @click="handleCreate" class="btn bg-gradient-to-r from-indigo-600 to-purple-600 text-white border-none hover:from-indigo-700 hover:to-purple-700 px-8 py-3 text-base font-semibold rounded-full shadow-md hover:shadow-lg transition-all duration-300 w-full sm:w-64">
            创建
          </button>
        </div>
      </div>
    </div>

  </div>
</template>

<style scoped>

</style>