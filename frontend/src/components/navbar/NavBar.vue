<script setup xmlns:RouterLink="http://www.w3.org/1999/html">
import MenuIcon from "@/components/navbar/icon/MenuIcon.vue";
import HomePageIcon from "@/components/navbar/icon/HomePageIcon.vue";
import FriendIcon from "@/components/navbar/icon/FriendIcon.vue";
import CameraIcon from "@/components/navbar/icon/CameraIcon.vue";
import CreateIcon from "@/components/navbar/icon/CreateIcon.vue";
import SearchIcon from "@/components/navbar/icon/SearchIcon.vue";
</script>

<template>
  <div class="drawer lg:drawer-open">
    <input id="my-drawer-4" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content">
      <!-- 美化后的 Navbar -->
      <nav class="navbar w-full bg-white/80 backdrop-blur-md shadow-sm border-b border-gray-200/60 sticky top-0 z-50">
        <div class="navbar-start gap-2">
          <label for="my-drawer-4" aria-label="open sidebar" class="btn btn-circle btn-ghost btn-sm">
            <MenuIcon class="w-5 h-5" />
          </label>
          <div class="font-bold text-xl bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent h-8/12 flex items-center">
            AI Friends
          </div>
        </div>

        <div class="navbar-center hidden md:flex w-4/5 max-w-180 flex justify-center">
          <div class="join w-4/5">
            <input
              class="input input-bordered join-item rounded-l-full w-4/5 focus:ring-2 focus:ring-indigo-200 transition-all"
              placeholder="搜索你感兴趣的内容"
            />
            <button class="btn join-item rounded-r-full bg-indigo-50 hover:bg-indigo-100 border-indigo-200 text-indigo-700 gap-1 px-5">
              <SearchIcon class="w-4 h-4" />
              <span class="hidden sm:inline">搜索</span>
            </button>
          </div>
        </div>

        <div class="navbar-end gap-2">
          <RouterLink :to="{name:'user-account-login-index'}" active-class="btn-active"
            class="btn btn-ghost text-base hover:bg-gray-100 hover:text-gray-900 active:bg-gray-200 transition-all duration-200 px-5 border border-gray-200 rounded-full"
          >
            登 录
          </RouterLink>
          <!-- 移动端搜索图标（小屏显示） -->
          <button class="btn btn-circle btn-ghost md:hidden">
            <SearchIcon class="w-5 h-5" />
          </button>
        </div>
      </nav>

      <!-- 页面内容区域（增加内边距，避免被固定导航遮挡） -->
      <main class="pt-4 px-4 md:px-6">
        <slot />
      </main>
    </div>

    <!-- 美化后的侧边栏抽屉 -->
    <div class="drawer-side">
      <label for="my-drawer-4" aria-label="close sidebar" class="drawer-overlay"></label>
      <div
        class="flex min-h-full flex-col items-start bg-white/90 backdrop-blur-md border-r border-gray-200 shadow-lg transition-all duration-300 is-drawer-close:w-16 is-drawer-open:w-64"
      >
        <!-- 侧边栏头部（显示logo简写） -->
        <div class="w-full p-4.5 flex justify-center items-center  border-b border-gray-200/60 ">
          <span class="font-bold text-xl text-indigo-600 is-drawer-close:hidden">AI Friends </span>
          <span class="font-bold text-xl text-indigo-600 is-drawer-open:hidden">AI</span>
        </div>

        <ul class="menu w-full grow p-2 space-y-1">
          <li>
            <RouterLink :to="{name:'homepage-index'}" active-class="menu-focus"
              class="is-drawer-close:tooltip is-drawer-close:tooltip-right py-3 px-4 rounded-lg hover:bg-indigo-50 hover:text-indigo-700 transition-colors whitespace-nowrap"
              data-tip="首页"
            >
              <HomePageIcon class="w-5 h-5" />
              <span class="is-drawer-close:hidden text-base ml-3 whitespace-nowrap">首页</span>
            </RouterLink>
          </li>
          <li>
            <RouterLink :to="{name:'friend-index'}" active-class="menu-focus"
              class="is-drawer-close:tooltip is-drawer-close:tooltip-right py-3 px-4 rounded-lg hover:bg-indigo-50 hover:text-indigo-700 transition-colors whitespace-nowrap"
              data-tip="好友"
            >
              <FriendIcon class="w-5 h-5" />
              <span class="is-drawer-close:hidden text-base ml-3 whitespace-nowrap">好友</span>
            </RouterLink>
          </li>
          <li>
            <RouterLink :to="{name:'create-index'}" active-class="menu-focus"
              class="is-drawer-close:tooltip is-drawer-close:tooltip-right py-3 px-4 rounded-lg hover:bg-indigo-50 hover:text-indigo-700 transition-colors whitespace-nowrap"
              data-tip="创作"
            >
              <CreateIcon class="w-5 h-5" />
              <span class="is-drawer-close:hidden text-base ml-3 whitespace-nowrap">创作</span>
            </RouterLink>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

