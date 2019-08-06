"""
요청 정보로 랜딩 페이지 html을 구성하는 작업을 담당하는 클래스
"""
import base64
import json

from bs4 import BeautifulSoup


class Default:
    def __init__(self, landing_config):
        self.default_html = f"""
                        <!DOCTYPE html>
                <html lang="ko-kr">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="x-ua-compatible" content="ie=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
                    <title>{landing_config['title']}</title>

                    <!-- Control the behavior of search engine crawling and indexing -->
                    <meta name="robots" content="index,follow"><!-- All Search Engines -->
                    <link rel="shortcut icon" href="https://landings.infomagazine.xyz/favicon.ico" type="image/x-icon">
                    <link rel="icon" href="https://landings.infomagazine.xyz/favicon.ico" type="image/x-icon">
                </head>
                <body>
                </body>
                </html>
                """
        self.default_stylesheets = """
                <link rel="stylesheet" href="https://assets.infomagazine.xyz/css/normalize.css">
                <style>
                *, ::after, ::before {
                    box-sizing: border-box;
                }

                body {
                    font-size: 2.2vw;
                }

                a {
                    text-decoration: none;
                    color: #000;
                }

                img {
                    width: 100%;
                    display: block;
                }

                input {
                    border: 1px solid #808080;
                }

                .section-container {
                    max-width: 1000px;
                    margin: 0 auto;
                }

                .landing-section {
                    position: relative;
                    width: 100%;
                    min-height: 1px;
                }

                .landing-object-block {
                    position: absolute;
                }

                .object-type-image {
                    overflow: hidden;
                    height: 0;
                }

                .object-type-form {
                    width: 100%;
                    position: relative;
                    background: transparent;
                    overflow: auto;
                }

                .object-type-form::before {
                    content: "";
                    width: 1px;
                    margin-left: -1px;
                    float: left;
                    height: 0;
                }

                .object-type-form::after {
                    content: "";
                    display: table;
                    clear: both;
                }

                .form-group {
                    position: absolute;
                    display: flex;
                    align-items: center;
                }

                .form-group-prepend {
                    display: flex;
                }

                .form-group-label {
                    display: flex;
                    width: 100%;
                    align-items: center;
                }

                .form-control {
                    width: 1%;
                    display: flex;
                    align-items: center;
                    flex: 1 1 auto;
                    height: 5vw;
                    border-radius: 0.5vw;
                }

                .form-button {
                    width: 100%;
                    border: 1px solid;
                    background-color: #fff;
                    cursor: pointer;
                    padding: 0.5vw;
                    border-radius: 0.5vw;
                }

                @media (min-width: 1000px) {
                    body {
                        font-size: 1.5rem;
                    }

                    .form-control {
                        height: 50px;
                        border-radius: 5px
                    }

                    .form-button {
                        height: 50px;
                        padding: 5px;
                        border-radius: 5px
                    }
                }
            </style>
                """
        self.default_scripts = """
                <script src="https://assets.infomagazine.xyz/vendor/js/jquery-3.4.1.js"></script>
                """
        self.layout_stylesheets = ""
        self.landing_scripts = ""


class StyleSheet(Default):
    def __init__(self, landing_config):
        self.landing_config = landing_config
        super(StyleSheet, self).__init__(landing_config)

    def _css_section_height(self, section_id=None, section_h=None):
        height = section_h / 10
        result = f"""
        section[data-section-id="{section_id}"] {{
            margin-bottom: calc({height}% - 1px);
        }}
        """
        self.layout_stylesheets += result

    def _css_object_block_size(self, section_id=None, object_id=None, layout_info=None):
        object_x = layout_info['position']['x']
        object_y = layout_info['position']['y']
        object_w = layout_info['position']['w']

        ob_x_ratio = object_x / 10
        ob_y_ratio = object_y / 10
        ob_width_ratio = object_w / 10
        result = f"""
        section[data-section-id="{section_id}"] > div[data-object-id="{object_id}"] {{
            margin-left: {ob_x_ratio}%;
            margin-top: {ob_y_ratio}%;
            width: {ob_width_ratio}%;
        }}
        """
        self.layout_stylesheets += result

    def _css_object_by_type_size(self, object_type=None, section_id=None, object_id=None, layout_info=None):
        object_w = layout_info['position']['w']
        object_h = layout_info['position']['h']

        object_image_url = ""
        if layout_info['image_data']:
            object_image_url = layout_info['image_data']

        result = f""""""
        if object_type == 1:
            result += f"""
            section[data-section-id="{section_id}"] > div[data-object-id="{object_id}"] > .object-type-image {{
                padding-top: calc({object_h} / {object_w} * 100%);
                background: url('{object_image_url}') center / 100% no-repeat;
            }}
            """
        elif object_type == 2:
            result += f"""
            section[data-section-id="{section_id}"] > div[data-object-id="{object_id}"] > .object-type-form {{
                padding-top: calc({object_h} / {object_w} * 100%);
            }}
            """
        # TODO 비디오타입 추 후 추가
        elif object_type == 3:
            result += """"""
        self.layout_stylesheets += result

    def _css_field_position(self, section_id=None, object_id=None, object_w=None, object_h=None, field_id=None,
                            field_info=None, field_position_set=None):
        field_x = field_position_set['x']
        field_y = field_position_set['y']
        field_w = field_position_set['w']
        field_h = field_position_set['h']

        field_x_ratio = round((field_x * 100) / object_w, 6)
        field_y_ratio = round((field_y * 100) / object_h, 6)
        field_w_ratio = round((field_w * 100) / object_w, 6)

        result = f"""
        section[data-section-id="{section_id}"] > div[data-object-id="{object_id}"] > form > div[data-form-filed-id="{field_id}"] {{
            top: {field_y_ratio}%;
            left: {field_x_ratio}%;
            width: {field_w_ratio}%;
        }}
        """
        self.layout_stylesheets += result

    def _css_field_label_size(self, section_id=None, object_id=None, field_info_list=None, form_group_id=None):
        field_name_list = [len(field['name'])
                           for field_index, field
                           in enumerate(field_info_list)
                           if int(field['form_group_id']) == int(form_group_id)]
        label_len_list = list(set(field_name_list))
        label_len_list.sort()

        # 적정 라벨 넓이 계산
        is_long_spacing = False
        standard_len = label_len_list[0]
        diff_tmp = standard_len
        for index in range(1, len(label_len_list)):
            diff = label_len_list[index] - label_len_list[index - 1]

            if diff == diff_tmp or (diff < diff_tmp and not is_long_spacing):
                standard_len = label_len_list[index]

            if diff > diff_tmp:
                standard_len = label_len_list[index - 1]
                is_long_spacing = True
            diff_tmp = diff

        result = f"""
        section[data-section-id="{section_id}"] > div[data-object-id="{object_id}"] .form-group-prepend {{
            width: {standard_len * 3}vw;
        }}
        @media (min-width: 1000px) {{
            section[data-section-id="{section_id}"] > div[data-object-id="{object_id}"] .form-group-prepend {{
                width: {standard_len * 30}px;
            }}
        }}
        """
        self.layout_stylesheets += result

    def _stylesheets_generate(self):
        result = self.default_stylesheets
        result += f"""<style>{self.layout_stylesheets}</style>"""
        return result


class Script(Default):
    def __init__(self, landing_config):
        self.landing_config = landing_config
        super(Script, self).__init__(landing_config)

    def _js_init_datepicker(self, field_id=None):
        result = f"""
        $('#{field_id}').datepicker({{
            format: 'yyyy-mm-dd',
            date: new Date(1989, 6, 20),
            yearFirst: true,
            language: 'ko-KR',
            autoHide: true
        }});
        """
        self.landing_scripts += result

    def _js_submit_event(self, section_id=None, item_group=None):
        converted_item_group = {}
        for item in item_group:
            if item['type'] == 9 and 'required' in item['validation']:
                item['validation'].append('checked')
            converted_item_group[item['name']] = {'target': item['target'], 'validation': item['validation']}

        result = f"""
        $("#form_{section_id}_submit_button").click(function () {{
            var item_group = {json.dumps(converted_item_group)};
            form_{section_id}_validation(item_group);
            call_form_{section_id}_ajax(item_group)
        }});
        """
        self.landing_scripts += result

    def _js_validation(self, section_id=None):
        result = f"""
        function form_{section_id}_validation(item_group) {{
            // required
            // korean_only
            // english_only
            // number_only
            // email
            // phone_only
            // age_limit

            var required_list = [];
            var only_korean_list = [];
            var only_english_list = [];
            var only_num_list = [];
            var email_list = [];
            var tel_num_list = [];
            var age_limit_list = [];
            var checked_list = [];
            Object.entries(item_group).forEach(function (item) {{
                var _target = eval(item[1]['target']);
                if (item[1]['validation'].indexOf('required') !== -1) {{
                    if (item[1]['validation'].indexOf('checked') !== -1){{
                        if(!_target.is(":checked")){{
                            checked_list.push(_target.attr('data-label-name'))
                        }}
                    }}
                    if (!_target.val()) {{
                        required_list.push(_target.attr('data-label-name'));
                    }}
                }}
                if (item[1]['validation'].indexOf('korean_only') !== -1) {{
                    var only_korean_regex = /[^가-힣]/;
                    if (only_korean_regex.test(_target.val())) {{
                        only_korean_list.push(_target.attr('data-label-name'));
                    }}
                }}
                if (item[1]['validation'].indexOf('english_only') !== -1) {{
                    var only_english_regex = /[^a-zA-Z]/;
                    if (only_english_regex.test(_target.val())) {{
                        only_english_list.push(_target.attr('data-label-name'));
                    }}
                }}
                if (item[1]['validation'].indexOf('number_only') !== -1) {{
                    var only_num_regex = /[^0-9]/;
                    if (only_num_regex.test(_target.val())) {{
                        only_num_list.push(_target.attr('data-label-name'));
                    }}
                }}
                if (item[1]['validation'].indexOf('email') !== -1) {{
                    var email_regex = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{{2,3}}$/i;
                    if (!email_regex.test(_target.val())) {{
                        email_list.push(_target.attr('data-label-name'));
                    }}
                }}
                if (item[1]['validation'].indexOf('phone_only') !== -1) {{
                    var tel_num_regex = /^(010)\d{{3,4}}\d{{4}}$/;
                    if (!tel_num_regex.test(_target.val())) {{
                        tel_num_list.push(_target.attr('data-label-name'));
                    }}
                }}
                if (item[1]['validation'].indexOf('age_limit') !== -1) {{
                    var now_date = new Date();
                    var birthday_date = new Date(_target.val());
                    var new_now_date = new Date(now_date.getUTCFullYear() + "-" + (now_date.getUTCMonth() + 1) + "-" + now_date.getUTCDate());
                    var american_age_date = new Date((now_date.getUTCFullYear() - 19) + "-" + (now_date.getUTCMonth() + 1) + "-" + now_date.getUTCDate());
                    if (((now_date.getTime() + 32400000) - birthday_date.getTime()) < (new_now_date.getTime() - american_age_date.getTime())) {{
                        age_limit_list.push(_target.attr('data-label-name'));
                    }}
                }}
            }});
            validate_generator(required_list, "을(를) 입력해주세요.");
            validate_generator(only_korean_list, "은(는) 유효한 한글이 아닙니다.");
            validate_generator(only_english_list, "은(는) 유효한 영어가 아닙니다.");
            validate_generator(only_num_list, "은(는) 유효한 숫자가 아닙니다.");
            validate_generator(email_list, "은(는) 유효한 이메일이 아닙니다.");
            validate_generator(tel_num_list, "은(는) 유효한 전화번호가 아닙니다.");
            validate_generator(age_limit_list, "이(가) 만 19세 이하 제한에 걸립니다.");
            validate_generator(checked_list, "를 체크해주시기 바랍니다.");
            function validate_generator(list, message) {{
                if (list.length !== 0) {{
                    var list_total = "";
                    for (var i = 0; i < list.length; i++) {{
                        if (i === 0) {{
                            list_total += (list[i])
                        }} else {{
                            list_total += (", " + list[i])
                        }}
                    }}
                    alert(list_total + message);
                    throw list_total + message;
                }}
            }}
        }}
        """
        self.landing_scripts += result

    def _js_call_ajax(self, section_id=None):
        result = f"""
        function call_form_{section_id}_ajax(item_group) {{
            var body = {{
                'data': {{}},
                'schema': {{}}
            }};
            Object.entries(item_group).forEach(function (item) {{
                var _target = eval(item[1]['target']);
                body['data'][item[0]] = String(_target.val());
                body['schema'][item[0]] = _target.attr('data-label-name');
            }});
            body['landing_id'] = window.location.pathname.split('/')[1];
            body['registered_date'] = String(Date.now());
            $.ajax({{
                type: 'post',
                url: 'https://serverlessapi.infomagazine.xyz/db/',
                data: body,
                dataType: 'json',
                success: function (data) {{
                    if (data) {{
                        alert('신청이 완료되었습니다.');
                    }} else {{
                        alert("이미 신청하셨습니다.");
                    }}
                }},
                error: function (data) {{
                    alert('에러');
                }}
            }})
        }}
        """
        self.landing_scripts += result

    def _js_call_ajax_by_phone_auth(self, section_id=None):
        result = f"""
                function call_form_{section_id}_ajax(item_group) {{
                    var IMP = window.IMP;
                    IMP.init("imp77156252");
                    IMP.certification({{ // param
                        merchant_uid: "axa_img_tnk",
                        phone: $("#first_user_phone_1").val() + $("#first_user_phone_2").val() + $("#first_user_phone_3").val()
                    }}, function (rsp) {{ // callback
                        if (rsp.success) {{
                            $.ajax({{
                                type: 'get',
                                url: '',
                                data: {{imp_uid: rsp.imp_uid}},
                                dataType: 'json',
                                success: function (data) {{
                                    if (data) {{
                                        first_db_reg_ajax(data.data['name'], data.data['birth'], data.data['gender'])
                                        var body = {{
                                            'data': {{
                                                'form_{section_id}_name': data.data['name'],
                                                'form_{section_id}_birth': data.data['birth'],
                                                'form_{section_id}_gender': data.data['gender'],
                                            }},
                                            'schema': {{
                                                'form_{section_id}_name': '이름',
                                                'form_{section_id}_birth': '생년월일',
                                                'form_{section_id}_gender': '성별',
                                            }}
                                        }};
                                        Object.entries(item_group).forEach(function (item) {{
                                            var _target = eval(item[1]['target']);
                                            body['data'][item[0]] = _target.val();
                                            body['schema'][item[0]] = _target.attr('data-label-name');
                                        }});
                                        $.ajax({{
                                            type: 'post',
                                            url: 'https://api.infomagazine.xyz/db/',
                                            data: body,
                                            dataType: 'json',
                                            success: function (data) {{
                                                if (data) {{
                                                    alert('신청이 완료되었습니다.');
                                                }} else {{
                                                    alert("이미 신청하셨습니다.");
                                                }}
                                            }},
                                            error: function (data) {{
                                                alert('에러');
                                            }}
                                        }})
                                    }} else {{
                                        alert("인증 정보를 얻는데 실패하였습니다.");
                                    }}
                                }},
                                error: function (data) {{
                                    alert('일시적인 오류로 신청이 안 되었습니다.');
                                }}
                            }})
                            // first_db_reg_ajax()
                        }} else if (rsp.error_code === "F0000") {{
                            alert("인증 취소");
                        }} else {{
                            alert("인증에 실패하였습니다. 에러 내용: " + rsp.error_msg);
                        }}
                    }});
                }}
                """
        self.landing_scripts += result

    def _scripts_generate(self):
        result = self.default_scripts
        result += f"""
        <script>
        (function ($) {{
            {self.landing_scripts}
        }})(jQuery)
        </script>
        """

        return result


class LandingPage(StyleSheet, Script):
    def __init__(self, landing_info, is_generate=False):
        self.landing_config = landing_info['landing']
        super(LandingPage, self).__init__(landing_config=self.landing_config)
        self.term_config = landing_info['term']
        self.form_config_list = landing_info['form']
        self.field_info_list = landing_info['field']
        self.section_info_list = landing_info['sections']
        self.is_generate = is_generate

        self.is_datepicker_to_add = False
        self.is_phone_auth_to_add = False

    def _db_form_field_generator(self, base_html, section_id=None,
                                 object_id=None, object_w=None,
                                 object_h=None, field_id=None,
                                 field_info=None, field_position_set=None):
        """
        1: 텍스트 - input text
        2: 숫자 - input number
        3: 전화번호 - input number
        4: 선택 스크롤 - select, opt
        5: 선택 버튼 - radio
        6: 체크 박스 - chk
        7: 날짜 - date
        8: 완료버튼 - script
        9: 약관동의 - chk
        """
        self._css_field_position(section_id=section_id,
                                 object_id=object_id,
                                 object_w=object_w,
                                 object_h=object_h,
                                 field_id=field_id,
                                 field_info=field_info,
                                 field_position_set=field_position_set[
                                     'position'])
        form_group = base_html.new_tag('div', attrs={'class': 'form-group', 'data-form-filed-id': field_id})

        field_id = 'form_' + str(section_id) + '_' + base64.b16encode(field_info['name'].encode('utf-8')).decode(
            'utf-8')
        field_type = int(field_info['type'])

        if field_type == 1:
            label_wrap_tag = base_html.new_tag('div', attrs={'class': 'form-group-prepend'})
            label_tag = base_html.new_tag('label', attrs={'for': field_id,
                                                          'class': 'form-group-label'})
            label_tag.string = field_info['name']
            label_wrap_tag.append(label_tag)
            input_tag = base_html.new_tag('input', attrs={'type': 'text',
                                                          'id': field_id,
                                                          'class': 'form-control',
                                                          'data-label-name': field_info['name']})
            form_group.append(label_wrap_tag)
            form_group.append(input_tag)
        elif field_type == 2:
            label_wrap_tag = base_html.new_tag('div', attrs={'class': 'form-group-prepend'})
            label_tag = base_html.new_tag('label', attrs={'for': field_id,
                                                          'class': 'form-group-label'})
            label_tag.string = field_info['name']
            label_wrap_tag.append(label_tag)
            input_tag = base_html.new_tag('input', attrs={'type': 'number',
                                                          'id': field_id,
                                                          'class': 'form-control',
                                                          'data-label-name': field_info['name']})
            form_group.append(label_wrap_tag)
            form_group.append(input_tag)
        elif field_type == 3:
            label_wrap_tag = base_html.new_tag('div', attrs={'class': 'form-group-prepend'})
            label_tag = base_html.new_tag('label', attrs={'for': field_id,
                                                          'class': 'form-group-label'})
            label_tag.string = field_info['name']
            label_wrap_tag.append(label_tag)
            input_tag = base_html.new_tag('input', attrs={'type': 'tel',
                                                          'id': field_id,
                                                          'class': 'form-control',
                                                          'data-label-name': field_info['name']})
            form_group.append(label_wrap_tag)
            form_group.append(input_tag)
        elif field_type == 4:
            input_tag = base_html.new_tag('input', attrs={'type': 'select'})
            form_group.append(input_tag)
        elif field_type == 5:
            label_wrap_tag = base_html.new_tag('div', attrs={'class': 'form-group-prepend'})
            label_tag = base_html.new_tag('span', attrs={'class': 'form-group-label'})
            label_tag.string = field_info['name']
            label_wrap_tag.append(label_tag)
            form_group.append(label_wrap_tag)
            for radio_value in field_info['list']:
                radio_attrs = {
                    'type': 'radio',
                    'id': field_id,
                    'name': field_id,
                    'value': radio_value,
                    'data-label-name': field_info['name']
                }
                if field_info['default'] == radio_value:
                    radio_attrs['checked'] = ""
                radio_wrap_tag = base_html.new_tag('div', attrs={'class': 'form-control'})
                input_tag = base_html.new_tag('input', attrs=radio_attrs)
                label_tag = base_html.new_tag('label', attrs={'for': field_id,
                                                              'class': 'form-group-label'})
                label_tag.string = radio_value
                radio_wrap_tag.append(input_tag)
                radio_wrap_tag.append(label_tag)
                form_group.append(radio_wrap_tag)
        elif field_type == 6:
            input_tag = base_html.new_tag('input', attrs={'type': 'checkbox'})
            form_group.append(input_tag)
        elif field_type == 7:
            label_wrap_tag = base_html.new_tag('div',
                                               attrs={'class': 'form-group-prepend'})
            label_tag = base_html.new_tag('label', attrs={'for': field_id,
                                                          'class': 'form-group-label'})
            label_tag.string = field_info['name']
            label_wrap_tag.append(label_tag)
            input_tag = base_html.new_tag('input', attrs={'type': 'text',
                                                          'id': field_id,
                                                          'class': 'form-control',
                                                          'data-label-name': field_info['name'],
                                                          'data-toggle': 'datepicker',
                                                          'readonly': ''})
            form_group.append(label_wrap_tag)
            form_group.append(input_tag)
            self._js_init_datepicker(field_id=field_id)
            if not self.is_datepicker_to_add:
                self.default_stylesheets += """
                    <link rel="stylesheet" href="https://assets.infomagazine.xyz/vendor/css/datepicker.min.css">
                    """
                self.default_scripts += """
                    <script src="https://assets.infomagazine.xyz/vendor/js/datepicker.min.js"></script>
                    <script src="https://assets.infomagazine.xyz/vendor/js/datepicker.ko-KR.js"></script>
                    """
                self.is_datepicker_to_add = True
        elif field_type == 8:
            button_tag = base_html.new_tag('button', attrs={'type': 'button',
                                                            'class': 'form-button',
                                                            'id': "form_" + str(section_id) + "_submit_button"})
            button_tag.string = field_info['name']
            form_group.append(button_tag)
        elif field_type == 9:
            label_tag = base_html.new_tag('label', attrs={'for': field_id,
                                                          'class': 'form-group-label'})
            label_tag.string = field_info['holder']
            input_tag = base_html.new_tag('input', attrs={'type': 'checkbox',
                                                          'id': field_id,
                                                          'data-label-name': field_info['name']})
            form_group.append(input_tag)
            form_group.append(label_tag)
        return form_group, {
            'name': field_id,
            'type': field_info['type'],
            'target': f"""$('#{field_id}')""",
            'validation': list(field_info['validation'].keys())
        }

    def generate(self):
        """
        object_type == 1 : 이미지 객체
        object_type == 2 : 폼 객체
        object_type == 3 : 비디오 객체

        """
        base_html = BeautifulSoup(self.default_html, 'html.parser')

        main_container = base_html.new_tag('main', attrs={'class': 'section-container'})
        base_html.body.append(main_container)

        try:
            for section_index, section in enumerate(self.section_info_list):  # 섹션 생성
                section_h = section[0]['section_h']
                self._css_section_height(section_id=section_index,
                                         section_h=section_h)
                landing_section = base_html.new_tag('section',
                                                    attrs={'class': 'landing-section',
                                                           'data-section-id': section_index})
                main_container.append(landing_section)

                for object_index, section_object_info in enumerate(section):  # 객체 생성
                    self._css_object_block_size(section_id=section_index,
                                                object_id=object_index,
                                                layout_info=section_object_info)
                    section_object_block = base_html.new_tag('div', attrs={'class': 'landing-object-block',
                                                                           'data-object-id': object_index})
                    landing_section.append(section_object_block)
                    object_type = section_object_info['type']
                    self._css_object_by_type_size(object_type=object_type,
                                                  section_id=section_index,
                                                  object_id=object_index,
                                                  layout_info=section_object_info)
                    if object_type == 1:
                        section_object_by_type = base_html.new_tag('div', attrs={'class': 'object-type-image'})
                        section_object_block.append(section_object_by_type)

                    elif object_type == 2:
                        form_group_id = section_object_info['form_group_id']
                        self._css_field_label_size(section_id=section_index,
                                                   object_id=object_index,
                                                   field_info_list=self.field_info_list,
                                                   form_group_id=form_group_id)
                        section_object_by_type = base_html.new_tag('form', attrs={'class': 'object-type-form'})
                        section_object_block.append(section_object_by_type)
                        generated_field_list = [self._db_form_field_generator(base_html,
                                                                              section_id=section_index,
                                                                              object_id=object_index,
                                                                              object_w=section_object_info['position'][
                                                                                  'w'],
                                                                              object_h=section_object_info['position'][
                                                                                  'h'],
                                                                              field_id=field_index,
                                                                              field_info=field,
                                                                              field_position_set=next(
                                                                                  item for item in
                                                                                  section_object_info['fields']
                                                                                  if item["sign"] == field['sign']))
                                                for field_index, field
                                                in enumerate(self.field_info_list)
                                                if int(field['form_group_id']) == int(form_group_id)]

                        item_group = []
                        for generated_field, item in generated_field_list:
                            section_object_by_type.append(generated_field)
                            item_group.append(item)

                        self._js_submit_event(section_id=section_index,
                                              item_group=item_group)
                        self._js_validation(section_id=section_index)
                        self._js_call_ajax(section_id=section_index)

                    elif object_type == 3:
                        section_object_by_type = base_html.new_tag('div', attrs={'class': 'object-type-image'})
                        section_object_block.append(section_object_by_type)

            stylesheets = BeautifulSoup(self._stylesheets_generate(), 'html.parser')
            base_html.head.append(stylesheets)
            scripts = BeautifulSoup(self._scripts_generate(), 'html.parser')
            base_html.body.append(scripts)
            return {'state': True, 'data': base_html.prettify(), 'message': 'Succeed.'}
        except Exception as e:
            return {'state': False, 'data': '', 'message': str(e)}
