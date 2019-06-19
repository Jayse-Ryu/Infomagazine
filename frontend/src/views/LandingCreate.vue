<template>
  <div class="main">
    <div class="text_navigation">
      <router-link to="/">홈</router-link>
      <span>></span>
      <router-link to="/landing">랜딩 리스트</router-link>
      <span>></span>
      <router-link to="/landing/create">랜딩페이지 생성</router-link>
    </div>

    <div class="container" style="margin-top: 20px;">

      <form v-on:submit.prevent="landing_check">

        <h5>기본정보</h5>
        <section_basic
          :window_width="window_width"
          :company.sync="dynamo_obj.landing_info.landing.company"
          :name.sync="dynamo_obj.landing_info.landing.name"
          :base_url.sync="dynamo_obj.landing_info.landing.base_url"
          :error_name.sync="error_label.name"
          :error_base_url.sync="error_label.base_url"
        />

        <hr>

        <h5>DB 폼</h5>
        <section_form_control
          :form.sync="dynamo_obj.landing_info.form"
          :form_arrow.sync="form_arrow"
          :field.sync="dynamo_obj.landing_info.field"
        />
        <section_form_detail
          :window_width="window_width"
          :form_arrow.sync="form_arrow"
          :field.sync="dynamo_obj.landing_info.field"
        />

        <hr>

        <h5>추가내용</h5>
        <!--<section_term/>-->
        <!--<div class="form-group row mb-0">

          <label class="col-sm-3 col-form-label-sm mt-3" for="term_status">약관</label>

          <div class="col-sm-9 mt-sm-3">
            <label class="switch" for="term_status">
              <input type="checkbox" id="term_status" v-model="dynamo_obj.landing_info.landing.is_term">
              <span class="slider round"></span>
            </label>
          </div>

          <label v-if="dynamo_obj.landing_info.landing.is_term" class="col-sm-3 col-form-label-sm mt-3"
                 for="term_switch">
            약관 이미지
          </label>

          <div v-if="dynamo_obj.landing_info.landing.is_term" class="col-sm-9 mt-sm-3">
            <label class="switch" for="term_switch">
              <input type="checkbox" id="term_switch" v-model="dynamo_obj.landing_info.landing.image_term"
                     @change="term_file_delete()">
              <span class="slider round"></span>
            </label>
          </div>

        </div>

        <div class="form-group row"
             v-if="dynamo_obj.landing_info.landing.is_term && dynamo_obj.landing_info.landing.image_term">
          <label class="col-sm-3 col-form-label-sm mt-3" for="term_img">약관 이미지 파일</label>
          <div class="col-sm-9 mt-sm-3 row ml-0">
            <input type="file" class="input_one_btn form-control col-md-11 pt-1" id="term_img" placeholder="이미지"
                   ref="term_file_input" @change="term_file_add()" accept="image/*">
            <button type="button" class="btn btn-danger col-md-1 p-0" @click.prevent="term_file_delete()">삭제</button>
          </div>
        </div>

        <div class="form-group row"
             v-if="dynamo_obj.landing_info.landing.is_term && !dynamo_obj.landing_info.landing.image_term">
          <label class="col-sm-3 col-form-label-sm mt-3" for="term_title">약관 제목</label>
          <div class="col-sm-9 mt-sm-3">
            <input type="text" class="form-control" id="term_title" placeholder="title"
                   v-model="dynamo_obj.landing_info.term.title">
          </div>
          <label class="col-sm-3 col-form-label-sm mt-3" for="term_cont">약관 내용</label>
          <div class="col-sm-9 mt-sm-3">
                    <textarea type="text" class="form-control" id="term_cont" rows="4" placeholder="content"
                              v-model="dynamo_obj.landing_info.term.content"></textarea>
          </div>
        </div>
-->

        <hr>

        <h5>페이지 내용</h5>
        <div class="form-group row">

          <!--<section_page_source/>-->
          <!--<label class="col-sm-12 col-form-label-sm mt-3" for="page_title">
            <span>페이지 타이틀</span>
            <span class="question badge btn-secondary p-1 align-middle" v-if="window_width > 768"
                  v-tooltip="{
                  content: msg.title,
                  placement: 'right',
                  offset: 5,
                  trigger: 'hover',
                  }">?</span>
            <span class="question badge btn-secondary p-1" v-else
                  v-tooltip="{
                  content: msg.title,
                  placement: 'right',
                  offset: 5,
                  trigger: 'click',
                  }">?</span>
          </label>
          <div class="col-sm-12">
            <input type="text" class="form-control" id="page_title" maxlength="50"
                   v-model="dynamo_obj.landing_info.landing.title">
          </div>

          <label class="col-sm-3 col-form-label-sm mt-3" for="header_script">
            <span>헤더 스크립트</span>
          </label>
          <div class="col-sm-12">
            <textarea type="text" class="form-control" id="header_script" rows="4"
                      v-model="dynamo_obj.landing_info.landing.header_script"></textarea>
          </div>

          <label class="col-sm-3 col-form-label-sm mt-3" for="body_script">
            <span>바디 스크립트</span>
          </label>
          <div class="col-sm-12">
            <textarea type="text" class="form-control" id="body_script" rows="4"
                      v-model="dynamo_obj.landing_info.landing.body_script"></textarea>
          </div>
-->

          <!--<section_layout/>
          <section_layout_opt/>-->
          <!--
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

                  &lt;!&ndash;<img v-if="item.type == 1 && item.image_data.length == 0" src="../assets/logo1.png" alt="logo"
                       style="width: 100%; height: 100%; object-fit: contain;">
                  <img v-if="item.type == 1 && item.image_data.length !== 0" :src="item.image_url" alt="logo"
                       style="width: 100%; height: 100%; object-fit: contain;">&ndash;&gt;

                  &lt;!&ndash; Order layout for image &ndash;&gt;
                  <img v-if="item.type == 1 && !item.image_data.name" src="../assets/logo1.png" alt="logo_none"
                       style="width: 100%; height: 100%; object-fit: contain;">
                  <img v-if="item.type == 1 && item.image_data.name" :src="item.image_url" alt="logo_in"
                       style="width: 100%; height: 100%; object-fit: contain;">

                  &lt;!&ndash; Order layout for form group &ndash;&gt;
                  <div v-if="item.type == 2" class="form_layout" v-for="form in dynamo_obj.landing_info.form">
                    <div class="form_layout_cont" v-if="form.sign === item.form_group"
                         :style="'background:'+form.bg_color+';' + 'color:'+form.tx_color+';'+'z-index:10;'+'min-height: 100%;'">

                      &lt;!&ndash; big form &ndash;&gt;
                      <div class="form-group row mb-1" v-if="item.position.w > 768"
                           v-for="field in dynamo_obj.landing_info.field">

                        &lt;!&ndash; input form area &ndash;&gt;
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
                        &lt;!&ndash; /input form area &ndash;&gt;

                        &lt;!&ndash; button area &ndash;&gt;
                        <div class="pl-3 pr-3 pt-1 pb-1 col"
                             v-else-if="field.type == 7 || field.type == 8 || field.type == 9">
                          <div v-if="field.form_group_id == item.form_group">

                            &lt;!&ndash; link without image &ndash;&gt;
                            <button v-if="field.type == 7 && !field.image_url" type="button"
                                    class="btn w-100"
                                    :style="'background:'+field.back_color+';' + 'color:'+field.text_color+';'">
                              {{ field.holder }}
                            </button>
                            &lt;!&ndash; link with image &ndash;&gt;
                            <button v-else-if="field.type == 7 && field.image_url" type="button"
                                    class="btn w-100 p-0" style="background: transparent;">
                              <img :src="field.image_url" alt="button image" class="w-100 order_form_button_image">
                            </button>

                            &lt;!&ndash; tel without image &ndash;&gt;
                            <button v-if="field.type == 8 && !field.image_url" type="button"
                                    class="btn w-100"
                                    :style="'background:'+field.back_color+';' + 'color:'+field.text_color+';'">
                              {{ field.holder }}
                            </button>
                            &lt;!&ndash; tel with image &ndash;&gt;
                            <button v-else-if="field.type == 8 && field.image_url" type="button"
                                    class="btn w-100 p-0" style="background: transparent;">
                              <img :src="field.image_url" alt="button image" class="w-100 order_form_button_image">
                            </button>

                            &lt;!&ndash; submit without image &ndash;&gt;
                            <button v-if="field.type == 9 && !field.image_url" type="button"
                                    class="btn w-100"
                                    :style="'background:'+field.back_color+';' + 'color:'+field.text_color+';'">
                              {{ field.holder }}
                            </button>
                            &lt;!&ndash; submit with image &ndash;&gt;
                            <button v-else-if="field.type == 9 && field.image_url" type="button"
                                    class="btn w-100 p-0" style="background: transparent;">
                              <img :src="field.image_url" alt="button image" class="w-100 order_form_button_image">
                            </button>
                          </div>
                        </div>
                        &lt;!&ndash; /button area &ndash;&gt;
                      </div>
                      &lt;!&ndash; /big form &ndash;&gt;

                      &lt;!&ndash; small form &ndash;&gt;
                      <div class="form-group row mb-1" v-else-if="item.position.w < 769">
                        &lt;!&ndash; input form area &ndash;&gt;
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
                        &lt;!&ndash; /input form area &ndash;&gt;

                        &lt;!&ndash; button area &ndash;&gt;
                        <div class="pl-3 pr-3 pt-1 pb-1 col"
                             v-else-if="field.type == 7 || field.type == 8 || field.type == 9">
                          <div v-if="field.form_group_id == item.form_group">

                            &lt;!&ndash; link without image &ndash;&gt;
                            <button v-if="field.type == 7 && !field.image_url" type="button"
                                    class="btn w-100"
                                    :style="'background:'+field.back_color+';' + 'color:'+field.text_color+';'">
                              {{ field.holder }}
                            </button>
                            &lt;!&ndash; link with image &ndash;&gt;
                            <button v-else-if="field.type == 7 && field.image_url" type="button"
                                    class="btn w-100 p-0" style="background: transparent;">
                              <img :src="field.image_url" alt="button image" class="w-100 order_form_button_image">
                            </button>

                            &lt;!&ndash; tel without image &ndash;&gt;
                            <button v-if="field.type == 8 && !field.image_url" type="button"
                                    class="btn w-100"
                                    :style="'background:'+field.back_color+';' + 'color:'+field.text_color+';'">
                              {{ field.holder }}
                            </button>
                            &lt;!&ndash; tel with image &ndash;&gt;
                            <button v-else-if="field.type == 8 && field.image_url" type="button"
                                    class="btn w-100 p-0" style="background: transparent;">
                              <img :src="field.image_url" alt="button image" class="w-100 order_form_button_image">
                            </button>

                            &lt;!&ndash; submit without image &ndash;&gt;
                            <button v-if="field.type == 9 && !field.image_url" type="button"
                                    class="btn w-100"
                                    :style="'background:'+field.back_color+';' + 'color:'+field.text_color+';'">
                              {{ field.holder }}
                            </button>
                            &lt;!&ndash; submit with image &ndash;&gt;
                            <button v-else-if="field.type == 9 && field.image_url" type="button"
                                    class="btn w-100 p-0" style="background: transparent;">
                              <img :src="field.image_url" alt="button image" class="w-100 order_form_button_image">
                            </button>
                          </div>
                        </div>
                        &lt;!&ndash; /button area &ndash;&gt;
                      </div>
                      &lt;!&ndash; /small form &ndash;&gt;
                    </div>
                    &lt;!&ndash; /form_layout_cont &ndash;&gt;
                  </div>
                  &lt;!&ndash; /form_layout &ndash;&gt;


                  &lt;!&ndash; Order layout for video &ndash;&gt;
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
                &lt;!&ndash;<button type="button" class="btn btn-primary col-md-1 p-0">추가</button>&ndash;&gt;
                <button type="button" class="btn btn-danger col-md-1 p-0" @click.prevent="in_banner_file_delete()">
                  <span>삭제</span>
                </button>
              </div>
            </div>

          </div>-->
        </div>

        <hr>

        <h5>옵션</h5>
        <!--<section_page_opt/>-->
        <!--<div class="form-group row">
          <label class="col-sm-3 col-form-label-sm mt-3" for="status">활성상태</label>
          <div class="col-sm-9 mt-sm-3">
            <label class="switch" for="status">
              <input type="checkbox" id="status" v-model="dynamo_obj.landing_info.landing.is_active">
              <span class="slider round"></span>
            </label>
          </div>

          <label class="col-sm-3 col-form-label-sm mt-3" for="mobile">모바일 전용</label>
          <div class="col-sm-9 mt-sm-3">
            <label class="switch" for="mobile">
              <input type="checkbox" id="mobile" v-model="dynamo_obj.landing_info.landing.is_mobile">
              <span class="slider round"></span>
            </label>
          </div>

        </div>-->

        <hr>

        <div class="form-group row">
          <div class="col-12">
            <button type="submit" class="btn btn-primary col-12">생성</button>
            <button type="button" class="btn btn-dark col-12 mt-2" @click="back_to_list">취소</button>
          </div>
        </div>

      </form>

    </div>

    <!--<popup_recovery/>-->
    <!--&lt;!&ndash; When first access for create landing, show the company choice modal &ndash;&gt;
    <transition name="fade" mode="out-in">
      <div class="select_company_wrap" v-show="auto_flag">
        <div class="container company_list_box">

          <h4>임시저장된 랜딩페이지가 있습니다.</h4>

          <div class="form-group row">
            <label class="col-sm-3 col-form-label-sm mt-3" for="auto_id">
              <span>랜딩선택</span>
            </label>

            <div class="col-md-8 mt-sm-3">
              <select class="form-control" name="company" id="auto_id"
                      v-model="recovery">
                <option value="-1">선택하세요</option>
                <option v-for="content in auto_saved" :value="content.LandingNum">
                  {{content.landing_info.landing.company_name }} / {{ content.landing_info.landing.init_date }}
                </option>
              </select>
            </div>
            <div class="col-md-1 mt-sm-3 pl-md-0">
              <button type="button" class="btn btn-danger p-md-0 w-100 h-100" @click="auto_saved_delete">삭제</button>
            </div>
          </div>

          <button type="button" class="col btn btn-info mt-3" @click="auto_saved_detail">선택</button>
          <button type="button" class="btn btn-secondary col-12 mt-2" @click="auto_saved_not">선택 안함</button>
          <router-link to="/landing">
            <button type="button" class="btn btn-dark col-12 mt-2">취소</button>
          </router-link>
        </div>
      </div>
    </transition>-->
    <!--<popup_company/>-->
    <!--<transition name="fade" mode="out-in">
      <div class="select_company_wrap" v-show="company_flag">
        <div class="container company_list_box">

          <h4>고객업체를 먼저 선택해주세요.</h4>

          <div class="form-group row">
            <label class="col-sm-3 col-form-label-sm mt-3" for="company_id">
              <span>고객업체*</span>
            </label>

            <div class="col-sm-9 mt-sm-3">
              <select class="form-control" name="company" id="company_id"
                      v-model="dynamo_obj.landing_info.landing.company">
                <option value="-1">선택하세요</option>
                <option v-for="content in landing_company" :value="content.id">
                  {{content.name }} - {{ content.sub_name }}
                </option>
              </select>
            </div>
          </div>

          <button type="button" class="col btn btn-info mt-3" @click="first_check">선택</button>
          <router-link to="/landing">
            <button type="button" class="btn btn-dark col-12 mt-2">취소</button>
          </router-link>
        </div>
      </div>
    </transition>-->

  </div>
</template>

<script>
  import popup_recovery from '@/components/landing_create/popup_1_recovery.vue'
  import popup_company from '@/components/landing_create/popup_2_company.vue'
  import section_basic from '@/components/landing_create/section_1_basic.vue'
  import section_form_control from '@/components/landing_create/section_2_form_control.vue'
  import section_form_detail from '@/components/landing_create/section_3_form_detail.vue'
  import section_term from '@/components/landing_create/section_4_term.vue'
  import section_page_source from '@/components/landing_create/section_5_page_source.vue'
  import section_layout from '@/components/landing_create/section_6_layout.vue'
  import section_layout_opt from '@/components/landing_create/section_7_layout_opt.vue'
  import section_page_opt from '@/components/landing_create/section_8_page_opt.vue'

  export default {
    name: "landing_create",
    components: {
      // popup_recovery,
      // popup_company,
      section_basic,
      section_form_control,
      section_form_detail,
      // section_term,
      // section_page_source,
      // section_layout,
      // section_layout_opt,
      // section_page_opt
    },
    data: () => ({
      auto_flag: false,
      company_flag: false,
      window_width: window.innerWidth,
      // msg is Tooltip messages. 'msg' is static name by ToolTip api.
      msg: {
        // base_url: '기본 주소를 지정합니다.',
        title: '사이트 내부 제목입니다.',
        order: '랜딩페이지를 커스터마이징 합니다. 1000px 이상의 화면에서 작업대가 활성화됩니다.',
        in_db: '레이아웃 내부에 DB 폼 그룹을 위치시키거나 하단 팝업으로 대체합니다.',
        in_company: '랜딩 페이지에 하단 Footer로 해당 고객업체의 정보를 자동 기입합니다.',
        hijack: '사용자가 뒤로 가기 시 해당 링크로 강제 이동시킵니다.',
        in_banner: '스크롤 시 따라다니는 배너를 생성합니다.',
        // holder: 'Place holder입니다. 텍스트 입력 전 설명이 필요하거나 전화, 링크의 버튼에 표시할 글을 지정합니다.',
        list: '선택 옵션을 선택하고 제공할 수 있습니다.'
      },
      error_label: {
        name: true,
        base_url: true,
      },
      // Get org's companies and managers lists
      auto_saved: [],
      recovery: -1,
      landing_company: [],
      epoch_time: 0,
      // Landing obj
      dynamo_obj: {
        company_id: '',
        updated_date: '',
        landing_info: {
          landing: {
            company: -1,
            manager: -1,
            name: '',
            title: null,
            header_script: null,
            body_script: null,
            base_url: '',
            is_hijack: false,
            hijack_url: null,
            is_active: true,
            is_mobile: false,
            views: 0,
            collections: [],
            is_banner: false,
            banner_url: null,
            banner_image: null,
            inner_db: true,
            font: -1,
            is_term: false,
            image_term: false,
            show_company: false
          },
          term: {
            title: '',
            content: '',
            image: ''
          },
          form: [],
          field: [],
          order: []
        }
      },
      // Order relative
      order_focus_flag: false,
      order_selected: 0,
      // Form relative
      // form_temp: '',
      form_arrow: -1,
      form_selected: {
        sign: -1,
        bg_color: '#f9f9f9',
        tx_color: '#313131',
        opacity: 10
      },
      // Filter relative
      filtered_fields: [],
      field_selected: -1,
      field_temp_name: '',
    }),
    methods: {
      // Order handle
      // Order handle
      // Order handle
      order_add() {
        let len = this.dynamo_obj.landing_info.order.length
        if (len) {
          let highest = 0
          let z = 1
          for (let i = 0; i < len; i++) {
            if (this.dynamo_obj.landing_info.order[i].sign > highest) {
              highest = this.dynamo_obj.landing_info.order[i].sign
            }
          }
          for (let j = 0; j < len; j++) {
            if (this.dynamo_obj.landing_info.order[j].position.z > z) {
              z = this.dynamo_obj.landing_info.order[j].position.z
            }
          }
          let order_ready = {
            sign: highest + 1,
            type: 1,
            name: 'new layout',
            position: {x: 0, y: 0, w: 100, h: 100, z: z + 1},
            image_data: '',
            image_url: '',
            video_type: 1
          }
          this.dynamo_obj.landing_info.order.push(order_ready)
          alert('레이아웃이 생성되었습니다.')
        } else {
          let order_ready = {
            sign: 1,
            type: 1,
            name: 'new layout',
            position: {x: 0, y: 0, w: 100, h: 100, z: 1},
            image_data: '',
            image_url: '',
            video_type: 1
          }
          this.dynamo_obj.landing_info.order.push(order_ready)
          alert('레이아웃이 생성되었습니다.')
        }
      },
      order_delete() {
        if (this.order_selected) {
          if (confirm('선택한 레이아웃을 삭제하시겠습니까?')) {
            for (let i = 0; i < this.dynamo_obj.landing_info.order.length; i++) {
              if (this.dynamo_obj.landing_info.order[i].sign == this.order_selected) {
                if (i === 0) {
                  this.dynamo_obj.landing_info.order.shift()
                } else {
                  this.dynamo_obj.landing_info.order.splice(i, 1)
                }
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
      order_activated(sign) {
        this.order_selected = sign
        this.order_focus_flag = true
      },
      order_deactivated() {
        // this.order_selected = 0
        // this.order_focus_flag = false
      },
      order_move(x, y) {
        for (let i = 0; i < this.dynamo_obj.landing_info.order.length; i++) {
          if (this.dynamo_obj.landing_info.order[i].sign == this.order_selected) {
            this.dynamo_obj.landing_info.order[i].position.x = x
            this.dynamo_obj.landing_info.order[i].position.y = y
          }
        }
      },
      order_resize(x, y, w, h) {
        for (let i = 0; i < this.dynamo_obj.landing_info.order.length; i++) {
          if (this.dynamo_obj.landing_info.order[i].sign == this.order_selected) {
            this.dynamo_obj.landing_info.order[i].position.x = x
            this.dynamo_obj.landing_info.order[i].position.y = y
            this.dynamo_obj.landing_info.order[i].position.w = w
            this.dynamo_obj.landing_info.order[i].position.h = h
          }
        }
      },
      order_image_change(sign) {
        let file_data = event.target.files[0]
        for (let i = 0; i < this.dynamo_obj.landing_info.order.length; i++) {
          if (this.dynamo_obj.landing_info.order[i].sign == sign) {
            this.dynamo_obj.landing_info.order[i].image_data = file_data
            this.dynamo_obj.landing_info.order[i].image_url = URL.createObjectURL(file_data)
          }
        }
      },
      /* e */
      /* n */
      /* d */
      // File handle
      // File handle
      // File handle
      field_file_add(sign) {
        let file_data = event.target.files[0]
        for (let i = 0; i < this.dynamo_obj.landing_info.field.length; i++) {
          if (this.dynamo_obj.landing_info.field[i].sign == sign) {
            this.dynamo_obj.landing_info.field[i].image_data = file_data
            this.dynamo_obj.landing_info.field[i].image_url = URL.createObjectURL(file_data)
          }
        }
      },
      field_file_delete(sign) {
        document.getElementById('field_file_input' + sign).value = ''
        for (let i = 0; i < this.dynamo_obj.landing_info.field.length; i++) {
          if (this.dynamo_obj.landing_info.field[i].sign == sign) {
            this.dynamo_obj.landing_info.field[i].image_data = null
            this.dynamo_obj.landing_info.field[i].image_url = null
          }
        }
      },
      term_file_add() {
        /* When file data changed */
        let file_data = event.target.files[0]
        this.dynamo_obj.landing_info.term.image = file_data
      },
      term_file_delete() {
        /* Remove file data */
        if (this.$refs.term_file_input) {
          this.$refs.term_file_input.value = null
        }
        this.dynamo_obj.landing_info.term.image = null
      },
      in_banner_file_add() {
        /* When file data changed */
        let file_data = event.target.files[0]
        this.dynamo_obj.landing_info.landing.banner_image = file_data
      },
      in_banner_file_delete() {
        /* Remove file data */
        if (this.$refs.in_banner_file_input) {
          this.$refs.in_banner_file_input.value = null
        }
        this.dynamo_obj.landing_info.landing.banner_image = null
      },
      first_check() {
        // Empty filtering first

        // if (this.dynamo_obj.landing_info.landing.company == -1) {
        //   alert('업체를 선택하세요!')
        //   document.getElementById('company_id').focus()
        // } else {
        //   this.company_flag = false
        //   while (this.user_obj.id) {
        //     if (this.user_obj.id) {
        //       this.dynamo_obj.landing_info.landing.manager = this.user_obj.id
        //       if (this.epoch_time === 0) {
        //         this.epoch_time = Date.now()
        //       }
        //       this.collect_dynamo('first')
        //       break
        //     }
        //   }
        // }
      },
      landing_check() {
        // Start validate before create
        this.$validator.validateAll()
        console.log(this.user_obj)
        this.dynamo_obj.landing_info.landing.manager = this.user_obj.id

        // Empty filtering first
        if (this.dynamo_obj.landing_info.landing.company == -1) {
          alert('업체를 선택하세요!')
          document.getElementById('company_id').focus()
        } else if (this.dynamo_obj.landing_info.landing.manager == -1) {
          alert('관리자를 선택하세요!')
          document.getElementById('manager').focus()
        } else if (!this.dynamo_obj.landing_info.landing.name) {
          alert('랜딩페이지 이름을 입력하세요!')
          document.getElementById('landing').focus()
        } else if (this.duplicated_name_flag) {
          alert('랜딩페이지 이름이 이미 존재합니다!')
          document.getElementById('landing').focus()
        } else if (!this.dynamo_obj.landing_info.landing.base_url) {
          alert('메인 URL을 입력하세요!')
          document.getElementById('base_url').focus()
        } else if (this.duplicated_url_flag) {
          alert('메인 URL이 이미 존재합니다!')
          document.getElementById('base_url').focus()
        } else {
          if (this.dynamo_obj.landing_info.form.length > 0) {
            let flag = true
            for (let i = 0; i < this.dynamo_obj.landing_info.field.length; i++) {
              if (this.dynamo_obj.landing_info.field[i].name == '') {
                alert('폼 그룹의 필드 이름을 모두 입력해주세요!')
                document.getElementById('db_field').focus()
                flag = false
                return flag
              }
            }
            if (flag) {
              this.collect_dynamo('checked')
            }
          } else {
            this.collect_dynamo('checked')
          }
        }
      },
      collect_dynamo(option) {
        // option first(mounted) or checked(button clicked)
        let axios = this.$axios
        const config = {
          headers: {
            'Content-Type': 'application/json'
            // 'Content-Type': 'multipart/form-data'
          }
        }
        this.dynamo_obj.company_id = this.dynamo_obj.landing_info.landing.company.toString()
        // this.dynamo_obj.LandingNum = this.epoch_time.toString()
        this.dynamo_obj.updated_date = (Date.now()).toString()
        // Empty objects make as Null
        for (let key in this.dynamo_obj.landing_info.landing) {
          if (this.dynamo_obj.landing_info.landing.hasOwnProperty(key)) {
            if (this.dynamo_obj.landing_info.landing[key] === '' && typeof (this.dynamo_obj.landing_info.landing[key]) != 'boolean') {
              this.dynamo_obj.landing_info.landing[key] = null
            }
          }
        }
        for (let key in this.dynamo_obj.landing_info.form) {
          if (this.dynamo_obj.landing_info.form.hasOwnProperty(key)) {
            if (this.dynamo_obj.landing_info.form[key] === '' && typeof (this.dynamo_obj.landing_info.form[key]) != 'boolean') {
              this.dynamo_obj.landing_info.form[key] = null
            }
          }
        }
        for (let key in this.dynamo_obj.landing_info.field) {
          if (this.dynamo_obj.landing_info.field.hasOwnProperty(key)) {
            for (let j in this.dynamo_obj.landing_info.field[key]) {
              if (this.dynamo_obj.landing_info.field[key][j] === '') {
                this.dynamo_obj.landing_info.field[key][j] = null
              }
            }
          }
        }
        for (let key in this.dynamo_obj.landing_info.order) {
          if (this.dynamo_obj.landing_info.order.hasOwnProperty(key)) {
            for (let j in this.dynamo_obj.landing_info.order[key]) {
              if (this.dynamo_obj.landing_info.order[key][j] === '') {
                this.dynamo_obj.landing_info.order[key][j] = null
              }
            }
          }
        }
        for (let key in this.dynamo_obj.landing_info.term) {
          if (this.dynamo_obj.landing_info.term.hasOwnProperty(key)) {
            if (this.dynamo_obj.landing_info.term[key] === '' && typeof (this.dynamo_obj.landing_info.term[key]) != 'boolean') {
              this.dynamo_obj.landing_info.term[key] = null
            }
          }
        }

        // console.log('axios temporary disabled')
        // console.log(this.dynamo_obj)
        this.$store.state.pageOptions.loading = true
        console.log('landing create object is? ', this.dynamo_obj)
        axios.post(this.$store.state.endpoints.baseUrl + 'landing_pages/', this.dynamo_obj, config)
          .then(() => {
            this.$store.state.pageOptions.loading = false
            if (option == 'checked') {
              alert('랜딩이 생성되었습니다.')
              this.bye()
            }
          })
          .catch((error) => {
            if (option == 'checked') {
              alert('랜딩 생성이 실패하였습니다.')
              this.$store.state.pageOptions.loading = false
            }
            console.log(error)
          })
      },
      /* e */
      /* n */
      /* d */
      // After Create
      // After Create
      // After Create
      bye() {
        this.$router.currentRoute.meta.protect_leave = 'no'
        this.$router.push({
          name: 'landing_list',
        })
      },
      /* e */
      /* n */
      /* d */
      back_to_list() {
        if (confirm('정말 취소하시겠습니까?')) {
          let axios = this.$axios
          let landing_num = this.epoch_time
          axios.delete(this.$store.state.endpoints.baseUrl + 'landings/api/' + landing_num)
            .then(() => {
              alert('목록으로 돌아갑니다.')
              this.$router.currentRoute.meta.protect_leave = 'no'
              this.$router.push({name: 'landing_list'})
            })
            .catch((error) => {
              console.log(error)
            })
        }
      },
      preview() {
        let axios = this.$axios
        let landing_num = this.$route.params.landing_id
        axios.get(this.$store.state.endpoints.baseUrl + 'landings/api/' + landing_num + '/?preview=true')
          .then((response) => {
            console.log('preview res', response)
          })
          .catch((error) => {
            console.log(error)
          })
      },
      auto_saved_get() {
        let axios = this.$axios
        // Check temporary saved landings
        let this_url = 'landings/api/'
        this.auto_saved = []
        this.$store.state.pageOptions.loading = true
        axios.get(this.$store.state.endpoints.baseUrl + this_url + '?auth=staff' + '&manager=' + this.user_obj.username + '&auto=true')
          .then((response) => {
            this.$store.state.pageOptions.loading = false
            let auto_flag = false
            for (let i = 0; i < response.data.length; i++) {
              if (response.data[i].landing_info.landing.name === null) {
                // auto saved list on
                auto_flag = true
                let temp_date = response.data[i].UpdatedTime
                let init_date = new Date(temp_date * 1)
                let date_string = init_date.getFullYear()
                if (init_date.getMonth() < 10) {
                  date_string += '-0' + init_date.getMonth()
                } else {
                  date_string += '-' + init_date.getMonth()
                }
                if (init_date.getDate() < 10) {
                  date_string += '-0' + init_date.getDate()
                } else {
                  date_string += '-' + init_date.getDate()
                }
                response.data[i].landing_info.landing.init_date = date_string
                this.auto_saved.push(response.data[i])
              }
            }
            if (auto_flag == true) {
              this.auto_flag = auto_flag
              this.company_flag = false
            } else {
              this.auto_flag = auto_flag
              this.company_flag = true
            }
          })
          .catch(() => {
            this.$store.state.pageOptions.loading = false
          })
      },
      auto_saved_delete() {
        if (this.recovery != -1) {
          let axios = this.$axios
          let landing_num = this.recovery
          axios.delete(this.$store.state.endpoints.baseUrl + 'landings/api/' + landing_num)
            .then(() => {
              this.recovery = -1
              this.auto_saved_get()
            })
            .catch((error) => {
              console.log(error)
              alert('삭제 중 에러가 발생하였습니다. 다시 시도해주세요.')
            })
        } else {
          alert('삭제 할 페이지를 먼저 선택하세요.')
        }
      },
      auto_saved_not() {
        if (confirm('무시하고 생성하시겠습니까?')) {
          this.$store.state.pageOptions.loading = false
          this.auto_flag = !this.auto_flag
          this.company_flag = !this.company_flag
        }
      },
      auto_saved_detail() {
        if (this.recovery != -1) {
          if (confirm('수정페이지로 이동 하시겠습니까?')) {
            this.$router.currentRoute.meta.protect_leave = 'no'
            this.$router.push({path: '/landings/detail/' + this.recovery})
          }
        } else {
          alert('수정 할 페이지를 먼저 선택하세요.')
        }
      }
    },
    mounted() {
      // Window width calculator
      let that = this
      this.$nextTick(function () {
        window.addEventListener('resize', function (e) {
          that.window_width = window.innerWidth
        })
      })

      // Get company, manager
      let axios = this.$axios
      // Check if this manager has auto saved landing page

      // this.auto_saved_get()

      // Get companies from logged in user's organization
      // let this_url = 'companies/'
      // // axios.get(this.$store.state.endpoints.baseUrl + this_url + '?organization=' + this.user_obj.info.organization)
      // axios.get(this.$store.state.endpoints.baseUrl + 'companies/')
      //   .then((response) => {
      //     console.log(response)
      //     this.landing_company = response.data.data.results
      //   })
      //   .catch((error) => {
      //     console.log(error)
      //   })
    },
    computed: {
      user_obj() {
        // Get user information
        let local_user = localStorage.getItem('authUser')
        let user_json = {}

        if (!local_user) {
          // dummy block access auth
          user_json = {
            'is_staff': false,
            'is_superuser': false,
            'access_role': 3,
            'failed': true
          }
        } else {
          user_json = JSON.parse(local_user)
        }

        return user_json
      },
      order_wrap_height() {
        let highest = 450
        for (let i = 0; i < this.dynamo_obj.landing_info.order.length; i++) {
          let sum = this.dynamo_obj.landing_info.order[i].position.y + this.dynamo_obj.landing_info.order[i].position.h
          if (sum > highest) {
            highest = sum + 50
          }
        }
        return highest
      }
    }
  }
</script>

<style lang="scss">
  hr {
    width: 100%;
  }

  /* ios switch */
  .switch {
    position: relative;
    display: inline-block;
    width: 60px;
    height: 34px;
  }

  /* Hide default HTML checkbox */
  .switch input {
    opacity: 0;
    width: 0;
    height: 0;
  }

  /* The slider */
  .slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #ccc;
    -webkit-transition: .4s;
    transition: .4s;
  }

  .slider:before {
    position: absolute;
    content: "";
    height: 26px;
    width: 26px;
    left: 4px;
    bottom: 4px;
    background-color: white;
    -webkit-transition: .4s;
    transition: .4s;
  }

  input:checked + .slider {
    background-color: #287BFF;
  }

  input:focus + .slider {
    box-shadow: 0 0 1px #287BFF;
  }

  input:checked + .slider:before {
    -webkit-transform: translateX(26px);
    -ms-transform: translateX(26px);
    transform: translateX(26px);
  }

  .slider.round {
    border-radius: 34px;
  }

  .slider.round:before {
    border-radius: 50%;
  }

  .term_label {
    display: inline-block;
  }

  /*====*/

  /* margin dummy div */
  .margin_div {
    display: inline-block;
    width: 4%;
  }

  @media (max-width: 768px) {
    .margin_div {
      display: none;
    }
  }

  /*==*/

  .input_one_btn {
    max-width: 720px;
    margin-right: auto;
  }

  .layout_control {
    width: 60px;
    height: 30px;
    padding: 0;
    margin: 5px 0 5px 5px;
    font-size: 19px;
    font-weight: bold;
  }

  .landing_layout {
    background-color: #dedede;
    border-radius: 4px;
    min-height: 140px;
  }

  .layout_item {
    background-color: #efefef;
    border-radius: 8px;
    overflow: hidden;
  }

  .item_area {
    width: 100%;
    height: 100%;
    transition: all 250ms ease-out;
  }

  .color_wrap {
    overflow: hidden;
  }

  .color_picker {
    position: relative;
    width: 500%;
    height: 300%;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }

  .main_layout {
    border: 1px solid #ced4da;
    border-radius: 0.25rem;
    overflow: auto;
    transition: all 200ms ease-in-out;
  }

  .basket {
    border: 1px solid #ee5151;
    width: 1000px;
    min-height: 500px;
    overflow-x: hidden;
    overflow-y: auto;
    position: relative;
    margin: auto;
  }

  .drag_thing {
    /*position: absolute;*/
    /*display: inline-block;*/
    background-color: #eaeaea;
    border: 1px solid #818181;
  }

  .field_option_wrap {
    position: absolute;
    width: calc(100% - 10px);
    background-color: #fafafa;
    border: 1px solid #c1c1c1;
    border-radius: 8px;
    margin: auto;
    top: 40px;
    z-index: 900;
  }

  .console {
    width: 100%;
    max-width: 1000px;
    border: 1px solid #515151;
    margin: auto;
    background-color: #eaeaea;
  }

  .preview {
    width: 100%;
    margin: auto;
  }

  .video_handler {
    position: absolute;
    border-radius: 7px 0px 0px 7px;
    top: -1px;
    left: -104px;
    background-color: #515151;
    color: #e1e1e1;
    font-weight: bold;
    padding: 8px;
  }

  .video_handler_2 {
    position: absolute;
    border-radius: 0px 7px 7px 7px;
    bottom: -34px;
    right: -54px;
    background-color: #515151;
    color: #e1e1e1;
    font-weight: bold;
    padding: 8px;
  }

  .form_layout {
    position: absolute;
    width: 100%;
    height: 100%;
  }

  .form_layout_cont {
    position: relative;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    padding: 0 15px;
    overflow: auto;
    /*max-width: 750px;*/
  }

  .order_form_label {
    width: 25%;
  }

  .order_form_box {
    width: 75%;
    padding: 0 15px;
  }

  .select_company_wrap {
    position: fixed;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    background: rgba(0, 0, 0, 0.3);
    transition: 200ms visibility ease-in-out;
  }

  .company_list_box {
    background: #fff;
    padding: 25px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    border: 1px solid #eaeaea;
    border-radius: 8px;
  }

  .order_form_button_image {
    width: 100%;
    height: 100%;
    max-height: 50px;
    object-fit: contain;
  }

  /* The slider itself */
  .opacity_slider {
    -webkit-appearance: none; /* Override default CSS styles */
    appearance: none;
    background: #eaeaea; /* Grey background */
    outline: none; /* Remove outline */
    opacity: 0.9; /* Set transparency (for mouse-over effects on hover) */
    -webkit-transition: .2s; /* 0.2 seconds transition on hover */
    transition: opacity .2s;
    border-radius: 5px;
    padding: 0 0.25em;
  }

  /* Mouse-over effects */
  .opacity_slider:hover {
    opacity: 1; /* Fully shown on mouse-over */
  }

  /* The slider handle (use -webkit- (Chrome, Opera, Safari, Edge) and -moz- (Firefox) to override default look) */
  .opacity_slider::-webkit-slider-thumb {
    -webkit-appearance: none; /* Override default look */
    appearance: none;
    width: 30px; /* Set a specific slider handle width */
    height: 30px; /* Slider handle height */
    background: #17a2b8; /* Green background */
    cursor: pointer; /* Cursor on hover */
    border-radius: 5px;
  }

  .opacity_slider::-moz-range-thumb {
    width: 30px; /* Set a specific slider handle width */
    height: 30px; /* Slider handle height */
    background: #17a2b8; /* Green background */
    cursor: pointer; /* Cursor on hover */
    border-radius: 5px;
  }
</style>
