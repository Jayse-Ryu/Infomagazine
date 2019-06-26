<template>

  <div v-if="window_width > 999" class="form-group row">

    <label class="col-sm-3 col-form-label-sm mt-3" for="main_layout">
      <span>랜딩 레이아웃</span>
      <span class="question badge btn-secondary p-1 align-middle" v-if="window_width > 768"
            v-tooltip="{
                  content: msg.order,
                  placement: 'right',
                  offset: 5,
                  trigger: 'hover',
                  }">?</span>
      <span class="question badge btn-secondary p-1" v-else
            v-tooltip="{
                  content: msg.order,
                  placement: 'right',
                  offset: 5,
                  trigger: 'click',
                  }">?</span>
    </label>

    <div class="col-12 col-form-label mt-3">
      <button type="button" class="btn btn-primary p-1 w-100" @click="section_add">섹션추가</button>
    </div>

    <div class="col-12 p-0" v-for="(object, index) in order">
      <div class="col-sm-12 col-form-label-sm mt-3 text-right">
        <button type="button" class="btn btn-primary btn-sm p-1" @click.prevent="object_add(index)">객체 추가</button>
        <button type="button" class="btn btn-danger btn-sm p-1" @click.prevent="object_delete(index)">선택 삭제</button>
      </div>

      {{ order }}
      {{ object }}

      <div class="col-sm-12">
        <div class="main_layout" id="main_layout">
          <div class="basket" :style="{'height': order_wrap_height[index] + 'px'}">
            <vue-draggable-resizable v-for="item in object"
                                     @activated="order_activated(index, item.sign)"
                                     @deactivated="order_deactivated"
                                     @dragging="order_move"
                                     @resizing="order_resize"
                                     parent=".basket"
                                     class="drag_thing"
                                     class-name-dragging="drag_thing_drag"
                                     class-name-handle="drag_handle"
                                     :parent="false"
                                     :x="item.position.x"
                                     :y="item.position.y"
                                     :w="item.position.w"
                                     :h="item.position.h"
                                     :z="item.position.z"
                                     :min-width="100"
                                     :min-height="100"
                                     :grid=[10,10]
                                     :lock-aspect-ratio="false">

              <!--:key="item.sign"
                                     :sign="item.sign"-->

              <!--<img v-if="item.type == 1 && item.image_data.length == 0" src="../assets/logo1.png" alt="logo"
                   style="width: 100%; height: 100%; object-fit: contain;">
              <img v-if="item.type == 1 && item.image_data.length !== 0" :src="item.image_url" alt="logo"
                   style="width: 100%; height: 100%; object-fit: contain;">-->

              <!-- Order layout for image -->
              <img v-if="item.type == 1 && !item.image_data" src="../../assets/logo1.png" alt="logo_none"
                   style="width: 100%; height: 100%; object-fit: contain;">
              <img v-if="item.type == 1 && item.image_data" :src="item.image_data" alt="logo_in"
                   style="width: 100%; height: 100%; object-fit: contain;">

              <!-- Order layout for form group -->
              <div v-if="item.type == 2" class="form_layout" v-for="form in form">
                <div class="form_layout_cont" v-if="form.sign === item.form_group_id"
                     :style="'background:'+form.bg_color+';' + 'color:'+form.tx_color+';'+'z-index:10;'+'min-height: 100%;'">

                  <!-- big form -->
                  <div class="form-group row mb-1" v-if="item.position.w > 768"
                       v-for="field in field">

                    <!-- input form area -->
                    <div class="w-100 row m-0" v-if="field.type != 7 && field.type != 8 && field.type != 9">
                      <label v-if="field.form_group_id == item.form_group_id && field.label == true"
                             class="mt-3 text-center font-weight-bold pr-0 pt-2 order_form_label"
                             :for="'label'+field.name">
                        {{ field.name }}
                      </label>
                      <div v-if="field.form_group_id == item.form_group_id && field.label == true"
                           class="mt-sm-3 order_form_box">

                        <input v-if="field.type == 1" type="text" class="form-control" maxlength="0"
                               :placeholder="field.holder" :id="'label'+field.name">

                        <input v-if="field.type == 2" type="number" class="form-control" maxlength="0"
                               :placeholder="field.holder" :id="'label'+field.name">

                        <select v-if="field.type == 3" type="number" class="form-control" maxlength="0"
                                :placeholder="field.holder" :id="'label'+field.name">
                          <option value="0">select here</option>
                          <option v-for="list in field.list" :value="list">{{ list }}</option>
                        </select>

                        <div v-if="field.type == 4" :id="'label'+field.name"
                             class="form-check-inline d-flex flex-wrap ">
                          <div class="p-2" v-for="list in field.list">
                            <label class="form-check-label" :for="'field_' + list">
                              <input class="form-check-input" type="radio" :name="field.sign" :value="list"
                                     :id="'field_'+list">
                              {{ list }}
                            </label>
                          </div>
                        </div>

                        <div v-if="field.type == 5" :id="'label'+field.name"
                             class="form-check-inline d-flex flex-wrap ">
                          <div class="p-2" v-for="list in field.list">
                            <label class="form-check-label" :for="'field_' + list">
                              <input class="form-check-input" type="checkbox" :id="'field_' + list" :value="list">
                              {{ list }}
                            </label>
                          </div>
                        </div>

                        <input v-if="field.type == 6" type="text" class="form-control" disabled
                               placeholder="Datepicker" :id="'label'+field.name">

                        <div v-if="field.type == 10" :id="'label'+field.name"
                             class="form-check-inline d-flex flex-wrap ">
                          <div class="p-2">
                            <label class="form-check-label" :for="'term' + field.name">
                              <input class="form-check-input" type="checkbox" :id="'term'+field.name" value="1">
                              {{ field.holder }}
                            </label>
                            <button type="button" v-if="is_term"
                                    class="btn-sm btn-link p-0 border-0"
                                    style="line-height: 15px;">[{{ field.name }}]
                            </button>
                          </div>
                        </div>

                      </div>

                      <div v-else-if="field.form_group_id == item.form_group_id && field.label == false"
                           class="col-sm-12 mt-sm-3">

                        <input v-if="field.type == 1" type="text" class="form-control" maxlength="0"
                               :placeholder="field.holder" :id="'label'+field.name">

                        <input v-if="field.type == 2" type="number" class="form-control" maxlength="0"
                               :placeholder="field.holder" :id="'label'+field.name">

                        <select v-if="field.type == 3" type="number" class="form-control" maxlength="0"
                                :placeholder="field.holder" :id="'label'+field.name">
                          <option value="0">select here</option>
                          <option v-for="list in field.list" :value="list">{{ list }}</option>
                        </select>

                        <div v-if="field.type == 4" :id="'label'+field.name"
                             class="form-check-inline d-flex flex-wrap ">
                          <div class="p-2" v-for="list in field.list">
                            <label class="form-check-label" :for="'field_' + list">
                              <input class="form-check-input" type="radio" :name="field.sign" :value="list"
                                     :id="'field_'+list">
                              {{ list }}
                            </label>
                          </div>
                        </div>

                        <div v-if="field.type == 5" :id="'label'+field.name"
                             class="form-check-inline d-flex flex-wrap ">
                          <div class="p-2" v-for="list in field.list">
                            <label class="form-check-label" :for="'field_' + list">
                              <input class="form-check-input" type="checkbox" :id="'field_' + list" :value="list">
                              {{ list }}
                            </label>
                          </div>
                        </div>

                        <input v-if="field.type == 6" type="text" class="form-control" disabled
                               placeholder="Datepicker" :id="'label'+field.name">
                      </div>

                      <div v-if="field.type == 10" :id="'label'+field.name"
                           class="form-check-inline d-flex flex-wrap justify-content-end">
                        <div class="p-2">
                          <label class="form-check-label" :for="'term' + field.name">
                            <input class="form-check-input" type="checkbox" :id="'term'+field.name" value="1">
                            {{ field.holder }}
                          </label>
                          <button type="button" v-if="is_term"
                                  class="btn-sm btn-link p-0 border-0"
                                  style="line-height: 15px;">[{{ field.name }}]
                          </button>
                        </div>
                      </div>

                    </div>
                    <!-- /input form area -->

                    <!-- button area -->
                    <div class="pl-3 pr-3 pt-1 pb-1 col"
                         v-else-if="field.type == 7 || field.type == 8 || field.type == 9">
                      <div v-if="field.form_group_id == item.form_group_id">

                        <!-- link without image -->
                        <button v-if="field.type == 7 && !field.image_url" type="button"
                                class="btn w-100"
                                :style="'background:'+field.back_color+';' + 'color:'+field.text_color+';'">
                          {{ field.holder }}
                        </button>
                        <!-- link with image -->
                        <button v-else-if="field.type == 7 && field.image_url" type="button"
                                class="btn w-100 p-0" style="background: transparent;">
                          <img :src="field.image_url" alt="button image" class="w-100 order_form_button_image">
                        </button>

                        <!-- tel without image -->
                        <button v-if="field.type == 8 && !field.image_url" type="button"
                                class="btn w-100"
                                :style="'background:'+field.back_color+';' + 'color:'+field.text_color+';'">
                          {{ field.holder }}
                        </button>
                        <!-- tel with image -->
                        <button v-else-if="field.type == 8 && field.image_url" type="button"
                                class="btn w-100 p-0" style="background: transparent;">
                          <img :src="field.image_url" alt="button image" class="w-100 order_form_button_image">
                        </button>

                        <!-- submit without image -->
                        <button v-if="field.type == 9 && !field.image_url" type="button"
                                class="btn w-100"
                                :style="'background:'+field.back_color+';' + 'color:'+field.text_color+';'">
                          {{ field.holder }}
                        </button>
                        <!-- submit with image -->
                        <button v-else-if="field.type == 9 && field.image_url" type="button"
                                class="btn w-100 p-0" style="background: transparent;">
                          <img :src="field.image_url" alt="button image" class="w-100 order_form_button_image">
                        </button>
                      </div>
                    </div>
                    <!-- /button area -->
                  </div>
                  <!-- /big form -->

                  <!-- small form -->
                  <div class="form-group row mb-1" v-else-if="item.position.w < 769">
                    <!-- input form area -->
                    <div class="w-100 row m-0" v-if="field.type != 7 && field.type != 8 && field.type != 9">
                      <label v-if="field.form_group_id == item.form_group_id && field.label == true"
                             class="col-12 font-weight-bold pr-0 pt-2 order_form_label"
                             :for="'label'+field.name">
                        {{ field.name }}
                      </label>
                      <div v-if="field.form_group_id == item.form_group_id && field.label == true"
                           class="col-12 order_form_box">

                        <input v-if="field.type == 1" type="text" class="form-control" maxlength="0"
                               :placeholder="field.holder" :id="'label'+field.name">

                        <input v-if="field.type == 2" type="number" class="form-control" maxlength="0"
                               :placeholder="field.holder" :id="'label'+field.name">

                        <select v-if="field.type == 3" type="number" class="form-control" maxlength="0"
                                :placeholder="field.holder" :id="'label'+field.name">
                          <option value="0">select here</option>
                          <option v-for="list in field.list" :value="list">{{ list }}</option>
                        </select>

                        <div v-if="field.type == 4" :id="'label'+field.name"
                             class="form-check-inline d-flex flex-wrap ">
                          <div class="p-2" v-for="list in field.list">
                            <label class="form-check-label" :for="'field_' + list">
                              <input class="form-check-input" type="radio" :name="field.sign" :value="list"
                                     :id="'field_'+list">
                              {{ list }}
                            </label>
                          </div>
                        </div>

                        <div v-if="field.type == 5" :id="'label'+field.name"
                             class="form-check-inline d-flex flex-wrap ">
                          <div class="p-2" v-for="list in field.list">
                            <label class="form-check-label" :for="'field_' + list">
                              <input class="form-check-input" type="checkbox" :id="'field_' + list" :value="list">
                              {{ list }}
                            </label>
                          </div>
                        </div>

                        <input v-if="field.type == 6" type="text" class="form-control" disabled
                               placeholder="Datepicker" :id="'label'+field.name">

                        <div v-if="field.type == 10" :id="'label'+field.name"
                             class="form-check-inline d-flex flex-wrap">
                          <div class="p-2">
                            <label class="form-check-label" :for="'term' + field.name">
                              <input class="form-check-input" type="checkbox" :id="'term'+field.name" value="1">
                              {{ field.holder }}
                            </label>
                            <button type="button" v-if="is_term"
                                    class="btn-sm btn-link p-0 border-0"
                                    style="line-height: 15px;">[{{ field.name }}]
                            </button>
                          </div>
                        </div>

                      </div>

                      <div v-else-if="field.form_group_id == item.form_group_id && field.label == false"
                           class="col-sm-12 mt-sm-3">

                        <input v-if="field.type == 1" type="text" class="form-control" maxlength="0"
                               :placeholder="field.holder" :id="'label'+field.name">

                        <input v-if="field.type == 2" type="number" class="form-control" maxlength="0"
                               :placeholder="field.holder" :id="'label'+field.name">

                        <select v-if="field.type == 3" type="number" class="form-control" maxlength="0"
                                :placeholder="field.holder" :id="'label'+field.name">
                          <option value="0">select here</option>
                          <option v-for="list in field.list" :value="list">{{ list }}</option>
                        </select>

                        <div v-if="field.type == 4" :id="'label'+field.name"
                             class="form-check-inline d-flex flex-wrap ">
                          <div class="p-2" v-for="list in field.list">
                            <label class="form-check-label" :for="'field_' + list">
                              <input class="form-check-input" type="radio" :name="field.sign" :value="list"
                                     :id="'field_'+list">
                              {{ list }}
                            </label>
                          </div>
                        </div>

                        <div v-if="field.type == 5" :id="'label'+field.name"
                             class="form-check-inline d-flex flex-wrap ">
                          <div class="p-2" v-for="list in field.list">
                            <label class="form-check-label" :for="'field_' + list">
                              <input class="form-check-input" type="checkbox" :id="'field_' + list" :value="list">
                              {{ list }}
                            </label>
                          </div>
                        </div>

                        <input v-if="field.type == 6" type="text" class="form-control" disabled
                               placeholder="Datepicker" :id="'label'+field.name">

                        <div v-if="field.type == 10" :id="'label'+field.name"
                             class="form-check-inline d-flex flex-wrap justify-content-end">
                          <div class="p-2">
                            <label class="form-check-label" :for="'term' + field.name">
                              <input class="form-check-input" type="checkbox" :id="'term'+field.name" value="1">
                              {{ field.holder }}
                            </label>
                            <button type="button" v-if="is_term"
                                    class="btn-sm btn-link p-0 border-0"
                                    style="line-height: 15px;">[{{ field.name }}]
                            </button>
                          </div>
                        </div>

                      </div>

                    </div>
                    <!-- /input form area -->

                    <!-- button area -->
                    <div class="pl-3 pr-3 pt-1 pb-1 col"
                         v-else-if="field.type == 7 || field.type == 8 || field.type == 9">
                      <div v-if="field.form_group_id == item.form_group_id">

                        <!-- link without image -->
                        <button v-if="field.type == 7 && !field.image_url" type="button"
                                class="btn w-100"
                                :style="'background:'+field.back_color+';' + 'color:'+field.text_color+';'">
                          {{ field.holder }}
                        </button>
                        <!-- link with image -->
                        <button v-else-if="field.type == 7 && field.image_url" type="button"
                                class="btn w-100 p-0" style="background: transparent;">
                          <img :src="field.image_url" alt="button image" class="w-100 order_form_button_image">
                        </button>

                        <!-- tel without image -->
                        <button v-if="field.type == 8 && !field.image_url" type="button"
                                class="btn w-100"
                                :style="'background:'+field.back_color+';' + 'color:'+field.text_color+';'">
                          {{ field.holder }}
                        </button>
                        <!-- tel with image -->
                        <button v-else-if="field.type == 8 && field.image_url" type="button"
                                class="btn w-100 p-0" style="background: transparent;">
                          <img :src="field.image_url" alt="button image" class="w-100 order_form_button_image">
                        </button>

                        <!-- submit without image -->
                        <button v-if="field.type == 9 && !field.image_url" type="button"
                                class="btn w-100"
                                :style="'background:'+field.back_color+';' + 'color:'+field.text_color+';'">
                          {{ field.holder }}
                        </button>
                        <!-- submit with image -->
                        <button v-else-if="field.type == 9 && field.image_url" type="button"
                                class="btn w-100 p-0" style="background: transparent;">
                          <img :src="field.image_url" alt="button image" class="w-100 order_form_button_image">
                        </button>
                      </div>
                    </div>
                    <!-- /button area -->
                  </div>
                  <!-- /small form -->
                </div>
                <!-- /form_layout_cont -->
              </div>
              <!-- /form_layout -->


              <!-- Order layout for video -->
              <div v-if="item.type == 3">
                <span class="video_handler">비디오 드래그</span>
                <span class="video_handler_2">비디오 드래그</span>
                <div
                  style="position: absolute; width: 100%; max-width: 1000px; margin: auto; left: 0; top: 50%; transform: translateY(-50%)">
                  <div style=" position: relative; padding-bottom: 56.25%; height:0;">
                    <iframe v-if="item.video_type == 1"
                            style="width: 100%; height: 100%; top:0; left:0; position: absolute;" type="text/html"
                            :src="'https://www.youtube.com/embed/'
                                + item.video_url
                                + '?&playlist=Ra8s0IHng6A&autoplay=0&loop=1&showinfo=0&fs=1&disablekb=1&vq=auto&controls=0&rel=0&iv_load_policy=3&mute=0&playsinline=1&modestbranding=1'"
                            frameborder="0" volume="1" allowfullscreen webkitallowfullscreen
                            mozallowfullscreen></iframe>
                    <iframe v-if="item.video_type == 2"
                            style="width: 100%; height: 100%; top:0; left:0; position: absolute;" type="text/html"
                            :src="'https://player.vimeo.com/video/' + item.video_url + '?&loop=1'" frameborder="0"
                            volume="1" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
                  </div>
                </div>
              </div>

            </vue-draggable-resizable>

          </div>

          <div class="console" v-if="order_focus_flag && order_selected != 0 && index == section_selected">
            <div v-for="info in object">

              <div class="form-group row p-4" v-if="info.sign == order_selected">
                <label for="console_type" class="col-sm-3 col-form-label-sm mt-3">타입</label>
                <div class="col-sm-9 mt-sm-3">
                  <select class="form-control" id="console_type" v-model.number="info.type">
                    <option value="1">이미지</option>
                    <option value="2">폼그룹</option>
                    <option value="3">비디오</option>
                  </select>
                </div>

                <label v-if="info.type == 3" for="video_type" class="col-sm-3 col-form-label-sm mt-3">
                  비디오 타입
                </label>
                <div v-if="info.type == 3" class="col-sm-9 mt-sm-3">
                  <select id="video_type" class="form-control" v-model="info.video_type">
                    <option value="1">Youtube</option>
                    <option value="2">Vimeo</option>
                  </select>
                </div>
                <label v-if="info.type == 1" class="col-sm-3 col-form-label-sm mt-3" for="image_set">
                  이미지 첨부
                </label>
                <label v-if="info.type == 2" class="col-sm-3 col-form-label-sm mt-3" for="form_set">
                  폼 그룹 선택
                </label>
                <label v-if="info.type == 3" class="col-sm-3 col-form-label-sm mt-3" for="video_set">
                  동영상 값
                </label>
                <div class="col-sm-9 mt-sm-3" id="choose_set">
                  <input v-if="info.type == 1" type="file" class="form-control p-1" id="image_set" accept="image/*"
                         @change="order_image_change(info.sign, $event.target.files[0])">
                  <button v-if="info.type == 1" type="button" class="btn btn-sm btn-danger w-100"
                  @click="order_image_delete(info.sign)">
                    이미지 삭제
                  </button>
                  <select v-if="info.type == 2" class="form-control" id="form_set" v-model="info.form_group_id">
                    <option value="0">폼 그룹을 선택하세요</option>
                    <option v-for="content in form" :value="content.sign">
                      {{ content.name }}
                    </option>
                  </select>
                  <input v-if="info.type == 3" type="text" class="form-control" id="video_set"
                         v-model="info.video_url">
                </div>

                <label for="console_x" class="col-sm-3 col-form-label-sm mt-3">X 좌표</label>
                <div class="col-sm-9 mt-sm-3">
                  <input type="number" id="console_x" v-model.number="info.position.x" class="form-control"
                         step="10">
                </div>

                <label for="console_y" class="col-sm-3 col-form-label-sm mt-3">Y 좌표</label>
                <div class="col-sm-9 mt-sm-3">
                  <input type="number" id="console_y" v-model.number="info.position.y" class="form-control"
                         step="10">
                </div>

                <label for="console_w" class="col-sm-3 col-form-label-sm mt-3">너비</label>
                <div class="col-sm-9 mt-sm-3">
                  <input type="number" id="console_w" v-model.number="info.position.w" class="form-control"
                         step="10">
                </div>

                <label for="console_h" class="col-sm-3 col-form-label-sm mt-3">높이</label>
                <div class="col-sm-9 mt-sm-3">
                  <input type="number" id="console_h" v-model.number="info.position.h" class="form-control"
                         step="10">
                </div>

                <label for="console_z" class="col-sm-3 col-form-label-sm mt-3">우선순위</label>
                <div class="col-sm-9 mt-sm-3">
                  <input type="number" id="console_z" v-model.number="info.position.z" class="form-control">
                </div>
              </div>
            </div>
          </div>

        </div>

        <div class="preview">
          <button type="button" class="btn btn-danger w-100" @click="section_delete(index)">섹션 삭제</button>
        </div>

      </div>

    </div>

    <div class="col-12 mt-3">
      <button type="button" class="btn btn-info w-100" @click="preview">미리보기</button>
    </div>

  </div>
</template>

<script>
  export default {
    name: "section_6_layout",
    props: [
      'window_width',
      'epoch_time',
      'order',
      'form',
      'field',
      'is_term',
      'push_landing'
    ],
    data: () => ({
      msg: {
        order: '랜딩페이지를 커스터마이징 합니다. 1000px 이상의 화면에서 작업대가 활성화됩니다.',
      },
      order_obj: [],
      order_focus_flag: false,
      section_selected: -1,
      order_selected: 0,
      console_height: []
    }),
    mounted() {
      this.order_obj = this.order
    },
    methods: {
      object_init() {
        this.order_obj = []
        this.order_obj = this.order
      },
      // Order handle
      // Order handle
      // Order handle
      section_add() {
        this.object_init()
        this.order_obj.push([])
        this.console_height.push({height: 450})
        this.$emit('update:order', this.order_obj)
      },
      section_delete(index) {
        this.object_init()
        this.order_obj.splice(index, 1)
        this.console_height.splice(index, 1)
        this.$emit('update:order', this.order_obj)
      },
      object_add(index) {
        this.object_init()
        if (this.order_obj[index].length == 0) {
          // If there is nothing in section list, add object immediately
          this.order_obj[index].push(
            {
              sign: 1,
              type: 1,
              video_type: null,
              form_group_id: null,
              section_h: 0,
              position: {
                x: 0,
                y: 0,
                w: 100,
                h: 100,
                z: 1
              },
              fields: [],
              image_data: null,
              video_url: null
            }
          )
        } else {
          // If there are objects in section list, add object with calculated z-index
          let sign = 1
          let highet = 1
          for (let i = 0; i < this.order_obj[index].length; i++) {
            if (this.order_obj[index][i].sign >= sign) {
              sign = this.order_obj[index][i].sign + 1
            }
            if (this.order_obj[index][i].position.z >= highet) {
              highet = this.order_obj[index][i].position.z + 1
            }
          }
          this.order_obj[index].push(
            {
              sign: sign,
              type: 1,
              video_type: null,
              form_group_id: null,
              section_h: 0,
              position: {
                x: 0,
                y: 0,
                w: 100,
                h: 100,
                z: highet
              },
              fields: [],
              image_data: null,
              video_url: null
            }
          )
        }

        this.$emit('update:order', this.order_obj)
      },
      object_delete(index) {
        this.object_init()
        if (this.order_selected) {
          if (confirm('선택한 레이아웃을 삭제하시겠습니까?')) {
            for (let i = 0; i < this.order_obj[index].length; i++) {
              if (this.order_obj[index][i].sign == this.order_selected) {
                if (i === 0) {
                  this.order_obj[index].shift()
                } else {
                  this.order_obj[index].splice(i, 1)
                }
                this.$emit('update:order', this.order_obj)
              }
            }
            let console_clear = {sign: 0, type: 0, name: '', position: {x: 0, y: 0, w: 0, h: 0, z: 0}}
            this.console_obj = console_clear
            this.order_selected = 0
            this.order_activated(0)
          }
        } else {
          alert('먼저 레이아웃을 선택하세요.')
        }
      },
      order_activated(index, sign) {
        this.section_selected = index
        this.order_selected = sign
        this.order_focus_flag = true
      },
      order_deactivated() {
        // // Nothing to do but component needed this method
        // this.order_selected = 0
        // this.order_focus_flag = false
      },
      order_move(x, y) {
        this.object_init()
        let compare = 0
        let sum = 0
        for (let i = 0; i < this.order_obj[this.section_selected].length; i++) {
          sum = this.order[this.section_selected][i].position.y + this.order[this.section_selected][i].position.h
          // Compare objects values
          if (compare < sum) {
            compare = sum
          }
          if (this.order_obj[this.section_selected][i].sign == this.order_selected) {
            this.order_obj[this.section_selected][i].position.x = x
            this.order_obj[this.section_selected][i].position.y = y
            this.order_obj[this.section_selected][i].section_h = compare
          }
        }
        this.$emit('update:order', this.order_obj)
      },
      order_resize(x, y, w, h) {
        this.object_init()
        let compare = 0
        let sum = 0
        for (let i = 0; i < this.order_obj[this.section_selected].length; i++) {
          sum = this.order[this.section_selected][i].position.y + this.order[this.section_selected][i].position.h
          // Compare objects values
          if (compare < sum) {
            compare = sum
          }
          if (this.order_obj[this.section_selected][i].sign == this.order_selected) {
            this.order_obj[this.section_selected][i].position.x = x
            this.order_obj[this.section_selected][i].position.y = y
            this.order_obj[this.section_selected][i].position.w = w
            this.order_obj[this.section_selected][i].position.h = h
            this.order_obj[this.section_selected][i].section_h = compare
          }
        }
        this.$emit('update:order', this.order_obj)
      },
      order_image_change(sign, file) {
        this.object_init()

        let key = require('../../../vue_env')

        AWS.config.update({
          region: key.BucketRegion,
          credentials: new AWS.CognitoIdentityCredentials({
            IdentityPoolId: key.IdentityPoolId
          })
        })

        let s3 = new AWS.S3(
          {
            apiVersion: '2008-10-17',
            params: {
              Bucket: key.AWS_STORAGE_BUCKET_NAME
            }
          }
        )

        let params = {
          Key: 'assets/images/landing/preview/' + this.epoch_time + '/section/' + file.lastModified + '_' + file.name,
          ContentType: file.type,
          Body: file,
          ACL: 'public-read'
        }

        s3.upload(params, (error, data) => {
          if (error) {
            console.log('S3 method error occurred', error)
          } else {
            // console.log('S3 method success', data)
            for (let i = 0; i < this.order_obj[this.section_selected].length; i++) {
              if (this.order_obj[this.section_selected][i].sign == sign) {
                this.order_obj[this.section_selected][i].image_data = params.Key
              }
            }
            this.$emit('update:order', this.order_obj)
            this.push_landing()
          }
        })




      },
      order_image_delete(sign) {
        this.object_init()

      },
      preview() {
        // let axios = this.$axios
        let landing_num = this.$route.params.landing_id
        axios.get(this.$store.state.endpoints.baseUrl + 'landings/api/' + landing_num + '/?preview=true')
          .then((response) => {
            console.log('preview res', response)
          })
          .catch((error) => {
            console.log(error)
          })
      },
    },
    computed: {
      order_wrap_height() {
        // Calculation layout section editor height
        let height = []
        let lowest = 450
        let compare = 0

        // Section parts
        for (let i = 0; i < this.order.length; i++) {
          compare = 0

          // Object parts
          for (let j = 0; j < this.order[i].length; j++) {
            let sum = this.order[i][j].position.y + this.order[i][j].position.h
            // Compare objects values
            if (compare < sum) {
              compare = sum
            }
          }

          // Set height
          if (compare > lowest) {
            height[i] = compare + 50
          } else {
            height[i] = lowest
          }
        }
        return height
      }
    }
  }
</script>

<style scoped>

</style>
