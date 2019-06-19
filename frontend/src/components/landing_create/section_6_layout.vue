<template>

  <div>

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
    <div class="col-sm-9 col-form-label-sm mt-3 text-right" v-if="window_width > 999">
      <button type="button" class="btn btn-primary btn-sm p-1" @click.prevent="order_add">객체 추가</button>
      <button type="button" class="btn btn-danger btn-sm p-1" @click.prevent="order_delete">선택 삭제</button>
    </div>
    <div class="col-sm-12">
      <div class="main_layout" v-if="window_width > 999" id="main_layout">
        <div class="basket" :style="{'height': order_wrap_height + 'px'}">
          <vue-draggable-resizable v-for="item in dynamo_obj.landing_info.order"
                                   @activated="order_activated(item.sign)"
                                   @deactivated="order_deactivated"
                                   @dragging="order_move"
                                   @resizing="order_resize"
                                   parent=".basket"
                                   class="drag_thing"
                                   class-name-dragging="drag_thing_drag"
                                   class-name-handle="drag_handle"
                                   :key="item.sign"
                                   :sign="item.sign"
                                   :parent="false"
                                   :x="item.position.x"
                                   :y="item.position.y"
                                   :w="item.position.w"
                                   :h="item.position.h"
                                   :z="item.position.z"
                                   :min-width="100"
                                   :min-height="100"
                                   :grid=[5,5]
                                   :lock-aspect-ratio="false">

            <!--<img v-if="item.type == 1 && item.image_data.length == 0" src="../assets/logo1.png" alt="logo"
                 style="width: 100%; height: 100%; object-fit: contain;">
            <img v-if="item.type == 1 && item.image_data.length !== 0" :src="item.image_url" alt="logo"
                 style="width: 100%; height: 100%; object-fit: contain;">-->

            <!-- Order layout for image -->
            <img v-if="item.type == 1 && !item.image_data.name" src="../../assets/logo1.png" alt="logo_none"
                 style="width: 100%; height: 100%; object-fit: contain;">
            <img v-if="item.type == 1 && item.image_data.name" :src="item.image_url" alt="logo_in"
                 style="width: 100%; height: 100%; object-fit: contain;">

            <!-- Order layout for form group -->
            <div v-if="item.type == 2" class="form_layout" v-for="form in dynamo_obj.landing_info.form">
              <div class="form_layout_cont" v-if="form.sign === item.form_group"
                   :style="'background:'+form.bg_color+';' + 'color:'+form.tx_color+';'+'z-index:10;'+'min-height: 100%;'">

                <!-- big form -->
                <div class="form-group row mb-1" v-if="item.position.w > 768"
                     v-for="field in dynamo_obj.landing_info.field">

                  <!-- input form area -->
                  <div class="w-100 row m-0" v-if="field.type != 7 && field.type != 8 && field.type != 9">
                    <label v-if="field.form_group_id == item.form_group && field.label == true"
                           class="mt-3 text-center font-weight-bold pr-0 pt-2 order_form_label"
                           :for="'label'+field.name">
                      {{ field.name }}
                    </label>
                    <div v-if="field.form_group_id == item.form_group && field.label == true"
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
                          <button type="button" v-if="dynamo_obj.landing_info.landing.is_term"
                                  class="btn-sm btn-link p-0 border-0"
                                  style="line-height: 15px;">[{{ field.name }}]
                          </button>
                        </div>
                      </div>

                    </div>

                    <div v-else-if="field.form_group_id == item.form_group && field.label == false"
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
                        <button type="button" v-if="dynamo_obj.landing_info.landing.is_term"
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
                    <div v-if="field.form_group_id == item.form_group">

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
                    <label v-if="field.form_group_id == item.form_group && field.label == true"
                           class="col-12 font-weight-bold pr-0 pt-2 order_form_label"
                           :for="'label'+field.name">
                      {{ field.name }}
                    </label>
                    <div v-if="field.form_group_id == item.form_group && field.label == true"
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
                          <button type="button" v-if="dynamo_obj.landing_info.landing.is_term"
                                  class="btn-sm btn-link p-0 border-0"
                                  style="line-height: 15px;">[{{ field.name }}]
                          </button>
                        </div>
                      </div>

                    </div>

                    <div v-else-if="field.form_group_id == item.form_group && field.label == false"
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
                          <button type="button" v-if="dynamo_obj.landing_info.landing.is_term"
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
                    <div v-if="field.form_group_id == item.form_group">

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
                                + item.video_data
                                + '?&playlist=Ra8s0IHng6A&autoplay=0&loop=1&showinfo=0&fs=1&disablekb=1&vq=auto&controls=0&rel=0&iv_load_policy=3&mute=0&playsinline=1&modestbranding=1'"
                          frameborder="0" volume="1" allowfullscreen webkitallowfullscreen
                          mozallowfullscreen></iframe>
                  <iframe v-if="item.video_type == 2"
                          style="width: 100%; height: 100%; top:0; left:0; position: absolute;" type="text/html"
                          :src="'https://player.vimeo.com/video/' + item.video_data + '?&loop=1'" frameborder="0"
                          volume="1" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
                </div>
              </div>
            </div>

          </vue-draggable-resizable>

        </div>

        <div class="console" v-if="order_focus_flag && order_selected != 0">
          <div v-for="info in dynamo_obj.landing_info.order">
            <div class="form-group row p-4" v-if="info.sign == order_selected">
              <label for="console_name" class="col-sm-3 col-form-label-sm mt-3">이름</label>
              <div class="col-sm-9 mt-sm-3">
                <input type="text" id="console_name" v-model="info.name" class="form-control" step="5"
                       maxlength="30">
              </div>

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
                       @change="order_image_change(info.sign)">
                <select v-if="info.type == 2" class="form-control" id="form_set" v-model="info.form_group">
                  <option value="0">폼 그룹을 선택하세요</option>
                  <option v-for="content in dynamo_obj.landing_info.form" :value="content.sign">{{ content.name
                    }}
                  </option>
                </select>
                <input v-if="info.type == 3" type="text" class="form-control" id="video_set"
                       v-model="info.video_data">
              </div>

              <label for="console_x" class="col-sm-3 col-form-label-sm mt-3">X 좌표</label>
              <div class="col-sm-9 mt-sm-3">
                <input type="number" id="console_x" v-model.number="info.position.x" class="form-control"
                       step="5">
              </div>

              <label for="console_y" class="col-sm-3 col-form-label-sm mt-3">Y 좌표</label>
              <div class="col-sm-9 mt-sm-3">
                <input type="number" id="console_y" v-model.number="info.position.y" class="form-control"
                       step="5">
              </div>

              <label for="console_w" class="col-sm-3 col-form-label-sm mt-3">너비</label>
              <div class="col-sm-9 mt-sm-3">
                <input type="number" id="console_w" v-model.number="info.position.w" class="form-control"
                       step="5">
              </div>

              <label for="console_h" class="col-sm-3 col-form-label-sm mt-3">높이</label>
              <div class="col-sm-9 mt-sm-3">
                <input type="number" id="console_h" v-model.number="info.position.h" class="form-control"
                       step="5">
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
        <button type="button" class="btn btn-info w-100" @click="preview">미리보기</button>
      </div>

      <div class="form-group row mb-0">

        <label class="col-sm-3 col-form-label-sm mt-3" for="layout_font">
          <span>레이아웃 폰트</span>
        </label>
        <div class="col-sm-9 mt-sm-3 row ml-0">
          <select class="form-control" name="layout_font" id="layout_font"
                  v-model="dynamo_obj.landing_info.landing.font">
            <option value="-1">OS 기본</option>
            <option value="1">Sans-serif</option>
            <option value="2">나눔고딕 (Nanum Gothic)</option>
            <option value="3">나눔명조 (Nanum Myeongjo)</option>
            <option value="4">제주고딕 (Jeju Gothic)</option>
          </select>
        </div>

        <label class="col-sm-3 col-form-label-sm mt-3" for="in_db">
          <span>레이아웃 내 DB</span>
          <span class="question badge btn-secondary p-1 align-middle" v-if="window_width > 768"
                v-tooltip="{
                      content: msg.in_db,
                      placement: 'right',
                      offset: 5,
                      trigger: 'hover',
                      }">?</span>
          <span class="question badge btn-secondary p-1 align-middle" v-else
                v-tooltip="{
                      content: msg.in_db,
                      placement: 'right',
                      offset: 5,
                      trigger: 'click',
                      }">?</span>
        </label>
        <div class="col-sm-9 mt-sm-3">
          <label class="switch" for="in_db">
            <input type="checkbox" id="in_db" v-model="dynamo_obj.landing_info.landing.inner_db">
            <span class="slider round"></span>
          </label>
        </div>

        <label class="col-sm-3 col-form-label-sm mt-3" for="in_company">
          <span>사업자 표기</span>
          <span class="question badge btn-secondary p-1 align-middle" v-if="window_width > 768"
                v-tooltip="{
                      content: msg.in_company,
                      placement: 'right',
                      offset: 5,
                      trigger: 'hover',
                      }">?</span>
          <span class="question badge btn-secondary p-1 align-middle" v-else
                v-tooltip="{
                      content: msg.in_company,
                      placement: 'right',
                      offset: 5,
                      trigger: 'click',
                      }">?</span>
        </label>
        <div class="col-sm-9 mt-sm-3">
          <label class="switch" for="in_company">
            <input type="checkbox" id="in_company" v-model="dynamo_obj.landing_info.landing.show_company">
            <span class="slider round"></span>
          </label>
        </div>

        <label class="col-sm-3 col-form-label-sm mt-3" for="is_hijack">
          <span>후팝업</span>
          <span class="question badge btn-secondary p-1 align-middle" v-if="window_width > 768"
                v-tooltip="{
                      content: msg.hijack,
                      placement: 'right',
                      offset: 5,
                      trigger: 'hover',
                      }">?</span>
          <span class="question badge btn-secondary p-1 align-middle" v-else
                v-tooltip="{
                      content: msg.hijack,
                      placement: 'right',
                      offset: 5,
                      trigger: 'click',
                      }">?</span>
        </label>
        <div class="col-sm-9 mt-sm-3">
          <label class="switch" for="is_hijack">
            <input type="checkbox" id="is_hijack" v-model="dynamo_obj.landing_info.landing.is_hijack">
            <span class="slider round"></span>
          </label>
        </div>
        <label v-if="dynamo_obj.landing_info.landing.is_hijack" class="col-sm-3 col-form-label-sm mt-3"
               for="hijack">
          <span>후팝업 링크</span>
        </label>
        <div v-if="dynamo_obj.landing_info.landing.is_hijack" class="col-sm-9 mt-sm-3 row ml-0">
          <input type="text" class="form-control col" id="hijack" placeholder="후팝업 주소"
                 v-model="dynamo_obj.landing_info.landing.hijack_url">
          <hr>
        </div>

        <label class="col-sm-3 col-form-label-sm mt-3" for="in_banner">
          <span>띠배너</span>
          <span class="question badge btn-secondary p-1 align-middle" v-if="window_width > 768"
                v-tooltip="{content: msg.in_banner,
                      placement: 'right',
                      offset: 5,
                      trigger: 'hover',
                      }">?</span>
          <span class="question badge btn-secondary p-1 align-middle" v-else
                v-tooltip="{content: msg.in_banner,
                      placement: 'right',
                      offset: 5,
                      trigger: 'click',
                      }">?</span>
        </label>
        <div class="col-sm-9 mt-sm-3">
          <label class="switch" for="in_banner">
            <input type="checkbox" id="in_banner" v-model="dynamo_obj.landing_info.landing.is_banner"
                   @change="in_banner_file_delete()">
            <span class="slider round"></span>
          </label>
        </div>

        <label v-if="dynamo_obj.landing_info.landing.is_banner" class="col-sm-3 col-form-label-sm mt-3"
               for="in_banner_img">
          <span>띠배너 옵션</span>
        </label>
        <div v-if="dynamo_obj.landing_info.landing.is_banner" class="col-sm-9 mt-sm-3 row ml-0">

          <input type="file" class="form-control col-sm-5 col-md-5 pt-1" id="in_banner_img" placeholder="이미지"
                 ref="in_banner_file_input" @change="in_banner_file_add()" accept="image/*">
          <div class="margin_div"></div>
          <input type="text" class="form-control col-sm-7 col-md-5" id="in_banner_desc" placeholder="띠배너 주소"
                 v-model="dynamo_obj.landing_info.landing.banner_url">
          <div class="margin_div"></div>
          <!--<button type="button" class="btn btn-primary col-md-1 p-0">추가</button>-->
          <button type="button" class="btn btn-danger col-md-1 p-0" @click.prevent="in_banner_file_delete()">
            <span>삭제</span>
          </button>
        </div>
      </div>

    </div>

  </div>
</template>

<script>
  export default {
    name: "section_6_layout",
    props: [
      'window_width',
      'order'
    ],
    data: () => ({
      msg: {
        order: '랜딩페이지를 커스터마이징 합니다. 1000px 이상의 화면에서 작업대가 활성화됩니다.',
      }
    }),
  }
</script>

<style scoped>

</style>
