<script setup>
import {ref} from "vue";
import {useUserStore} from "@/stores/user.js";
import {useRouter} from "vue-router";
import api from "@/js/http/api.js";

const username=ref('')
const password=ref('')
const passwordConfirmed=ref('')
const errorMessage=ref('')

const user=useUserStore()
const router=useRouter()

async function handleRegister(){
  errorMessage.value=''
  if(!username.value.trim()){
    errorMessage.value='用户名不能为空'
  }else if(!password.value.trim()){
    errorMessage.value='密码不能为空'
  }else if(password.value.trim()!== passwordConfirmed.value.trim()){
    errorMessage.value='两次输入密码不一致'
  }else {
    try {
      const res=await api.post('/api/user/account/register/',{
        username:username.value,
        password:password.value,
      })
      const data=res.data
      if (data.result==='success'){
        user.setAccessToken(data.access)
        user.setUserInfo(data)
        await router.push({
          name:'homepage-index'
        })
      }else {
        errorMessage.value=data.result
      }
    }catch (err){

    }
  }
}

</script>

<template>
  <div class="flex justify-center mt-80">
     <form @submit.prevent="handleRegister" class="fieldset bg-white/90 backdrop-blur-sm border border-indigo-100 rounded-2xl w-full max-w-md shadow-xl p-6 transition-all hover:shadow-2xl">
      <!-- 标题区域（替换原 legend，更醒目） -->
      <div class="text-center mb-6">
        <h2 class="text-2xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">
          欢迎注册
        </h2>
        <p class="text-sm text-gray-500 mt-1">请注册您的账号</p>
      </div>

      <!-- 用户名 -->
      <label class="label">
        <span class="label-text font-medium text-gray-700">用户名</span>
      </label>
      <input
        v-model="username" type="text"
        class="input input-bordered w-full rounded-lg border-gray-200 focus:border-indigo-300 focus:ring-2 focus:ring-indigo-200 transition-all"
        placeholder="请输入用户名"
      />

      <!-- 密码 -->
      <label class="label mt-4">
        <span class="label-text font-medium text-gray-700">密码</span>
      </label>
      <input
        v-model="password" type="password"
        class="input input-bordered w-full rounded-lg border-gray-200 focus:border-indigo-300 focus:ring-2 focus:ring-indigo-200 transition-all"
        placeholder="请输入密码"
      />

       <!-- 确认密码 -->
      <label class="label mt-4">
        <span class="label-text font-medium text-gray-700">确认密码</span>
      </label>
      <input
        v-model="passwordConfirmed" type="password"
        class="input input-bordered w-full rounded-lg border-gray-200 focus:border-indigo-300 focus:ring-2 focus:ring-indigo-200 transition-all"
        placeholder="确认密码"
      />
       <p v-if="errorMessage" class="text-sm text-red-500 mt-1">{{errorMessage}}</p>
      <!-- 注册按钮 -->
      <button class="btn mt-6 w-full bg-gradient-to-r from-indigo-600 to-purple-600 text-white border-none hover:from-indigo-700 hover:to-purple-700 shadow-md hover:shadow-lg transition-all duration-200 rounded-lg py-3 text-base font-medium">
        注 册
      </button>


      <div class="flex justify-between items-center mt-4 text-sm">
        <RouterLink
          :to="{name:'user-account-login-index'}"
          class="ml-auto text-indigo-600 hover:text-indigo-800 hover:underline transition-colors font-medium"
        >
          回到登录页面
        </RouterLink>
      </div>
    </form>
  </div>

</template>

<style scoped>

</style>