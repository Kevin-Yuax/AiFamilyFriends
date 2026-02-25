<script setup>
import { useUserStore } from "@/stores/user.js";
import UserSpaceIcon from "@/components/navbar/icon/UserSpaceIcon.vue";
import UserProfileIcon from "@/components/navbar/icon/UserProfileIcon.vue";
import UserLogoutIcon from "@/components/navbar/icon/UserLogoutIcon.vue";
import api from "@/js/http/api.js";
import {useRouter} from "vue-router";

const user = useUserStore();
const router=useRouter()

function closeMenu() {
  const element = document.activeElement;
  if (element && element instanceof HTMLElement) element.blur();
}
async function handleLogou(){
  try {
    const res=await api.post('api/user/account/logout/')
    if(res.data.result==='success'){
      user.logout()
      await router.push({
        name:'homepage-index'
      })
    }
  }catch (err){

  }
}


</script>


<template>
  <div class="dropdown dropdown-end">
    <!-- 头像按钮：悬停缩放 + 光晕效果 -->
    <div tabindex="0" role="button" class="avatar btn btn-circle w-10 h-10 p-0 border-2 border-transparent hover:border-indigo-200 hover:scale-105 transition-all duration-200 shadow-sm hover:shadow-md">
      <div class="w-12 rounded-full">
        <img :src="user.photo" alt="" class="object-cover" />
      </div>
    </div>

    <!-- 下拉菜单：毛玻璃背景 + 精致阴影 -->
    <ul
      tabindex="-1"
      class="dropdown-content menu bg-white/90 backdrop-blur-md rounded-2xl z-10 w-64 p-3 shadow-xl border border-gray-100 mt-2"
    >
      <!-- 用户信息卡片：头像 + 用户名 + 分割线 -->
      <li class="mb-1">
        <RouterLink
          @click="closeMenu"
          :to="{ name: 'user-space-index', params: { user_id: user.id } }"
          class="flex items-center gap-3 p-2 rounded-xl hover:bg-indigo-50 transition-colors"
        >
          <div class="avatar">
            <div class="w-14 rounded-full ring-2 ring-indigo-100 ring-offset-2">
              <img :src="user.photo" alt="" class="object-cover" />
            </div>
          </div>
          <span class="text-base font-semibold text-gray-800 line-clamp-1">{{ user.username }}</span>
        </RouterLink>
        <div class="divider my-1 h-px bg-gray-100"></div>
      </li>

      <!-- 菜单项：统一间距 + 图标与文字对齐 -->
      <li>
        <RouterLink
          @click="closeMenu"
          :to="{ name: 'user-space-index', params: { user_id: user.id } }"
          class="flex items-center gap-3 py-2.5 px-3 rounded-lg text-sm font-medium text-gray-700 hover:bg-indigo-50 hover:text-indigo-700 transition-colors"
        >
          <UserSpaceIcon class="w-5 h-5" />
          个人空间
        </RouterLink>
      </li>
      <li>
        <RouterLink
          @click="closeMenu"
          :to="{ name: 'user-space-index' ,params: { user_id: user.id } }"
          class="flex items-center gap-3 py-2.5 px-3 rounded-lg text-sm font-medium text-gray-700 hover:bg-indigo-50 hover:text-indigo-700 transition-colors"
        >
          <UserProfileIcon class="w-5 h-5" />
          编辑资料
        </RouterLink>
      </li>

      <!-- 退出登录：带分隔线，视觉区分 -->
      <li class="mt-1">
        <div class="divider my-1 h-px bg-gray-100"></div>
        <a @click="handleLogou"
          class="flex items-center gap-3 py-2.5 px-3 rounded-lg text-sm font-medium text-red-600 hover:bg-red-50 hover:text-red-700 transition-colors cursor-pointer"
        >
          <UserLogoutIcon class="w-5 h-5" />
          退出登录
        </a>
      </li>
    </ul>
  </div>
</template>

<style scoped>
/* 可选：自定义分割线（如果 DaisyUI 的 divider 不合用） */
.divider {
  margin: 0.25rem 0;
  width: 100%;
}
/* 确保图标颜色可继承父元素的 color */
:deep(svg) {
  transition: stroke 0.2s;
}
</style>