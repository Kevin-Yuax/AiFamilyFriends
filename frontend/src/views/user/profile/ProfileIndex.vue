<script setup>
import Photo from "@/views/user/profile/components/Photo.vue";
import Username from "@/views/user/profile/components/Username.vue";
import Profile from "@/views/user/profile/components/Profile.vue";
import { useUserStore } from "@/stores/user.js";
import {ref, useTemplateRef, watch} from "vue";
import {base64ToFile} from "@/js/utils/base_64-file.js";
import api from "@/js/http/api.js";

const user = useUserStore();
const photoRef=useTemplateRef('photo-ref')
const usernameRef=useTemplateRef('username-ref')
const profileRef=useTemplateRef('profile-ref')
const errorMessage=ref('')

// 新增：监听user仓库变化，强制同步子组件数据（解决子组件不刷新问题）
watch([() => user.username, () => user.profile, () => user.photo], () => {
  if (usernameRef.value) usernameRef.value.myUsername = user.username;
  if (profileRef.value) profileRef.value.myProfile = user.profile;
  if (photoRef.value) photoRef.value.myPhoto = user.photo;
}, { immediate: true }); // 立即执行，初始化时同步

async function handleUpdate(){
  const photo=photoRef.value.myPhoto
  const username=usernameRef.value.myUsername.trim()
  const profile=profileRef.value.myProfile.trim()
  errorMessage.value=''
  if (!photo){
    errorMessage.value='头像不能为空'
  }else if (!username){
    errorMessage.value='名称不能为空'
  }else if (!profile){
    errorMessage.value='简介不能为空'
  }else {
    const formData=new FormData()
    formData.append('username',username)
    formData.append('profile',profile)
    if(photo !== user.photo){
      formData.append('photo',base64ToFile(photo,'photo.png'))
    }
    try{
      const res=await api.post('/api/user/profile/update/',formData)
      const data=res.data

      if (data.result === 'success'){
        console.log('后端返回数据：', data);
        user.setUserInfo(data)
        errorMessage.value = '更新成功！';
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
  <div class="flex justify-center ">
    <div class="card bg-white/90 backdrop-blur-sm shadow-xl w-full max-w-lg border border-gray-200/60 transition-all hover:shadow-2xl mt-16">
      <div class="card-body p-6 md:p-8">
        <!-- 标题区域：渐变文字 + 装饰线 -->
        <div class="mb-6">
          <h2 class="text-2xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">
            编辑资料
          </h2>
          <div class="w-16 h-1 bg-gradient-to-r from-indigo-500 to-purple-500 rounded-full mt-2"></div>
        </div>

        <!-- 组件区域：统一间距，居中头像 -->


        <Photo ref="photo-ref" :photo="user.photo" />
        <Username ref="username-ref" :username="user.username" class="w-full" />
        <Profile ref="profile-ref" :profile="user.profile" class="w-full" />

        <p v-if="errorMessage" class="text-sm text-red-500">{{errorMessage}}</p>
        <!-- 按钮区域：全宽圆角 + 悬浮效果 -->
        <div class="card-actions justify-center mt-8">
          <button @click="handleUpdate" class="btn bg-gradient-to-r from-indigo-600 to-purple-600 text-white border-none hover:from-indigo-700 hover:to-purple-700 px-8 py-3 text-base font-semibold rounded-full shadow-md hover:shadow-lg transition-all duration-300 w-full sm:w-64">
            更新资料
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>