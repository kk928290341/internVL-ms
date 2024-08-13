from patch.generator_mixin_patch import patch_generator_mixin
from patch.modeling_attn_mask_utils_patch import patch_attn_mask

import mindspore as ms

from data_process import load_image
from internvl_chat.modeling_internvl_chat import InternVLChatModel
from internvl_chat.tokenization_internlm2 import InternLM2Tokenizer

mode = 0
ms.set_context(mode=mode, device_target='Ascend')
print(f'mode: {mode}')

patch_attn_mask()
patch_generator_mixin()

path = "/home/hukang/models/internVL/Mini-InternVL-Chat-2B-V1-5/"

model = InternVLChatModel.from_pretrained(path)
tokenizer = InternLM2Tokenizer.from_pretrained(path)


# set the max number of tiles in `max_num`
pixel_value = load_image('./examples/image3.jpg', max_num=12)
pixel_values = ms.Tensor(pixel_value, dtype=ms.float16)

generation_config = dict(
    num_beams=1,
    max_new_tokens=1024,
    do_sample=False,
)

# for name, value in model.named_parameters():
#     print(name, value.shape)
# exit()
# single-round single-image conversation
question = "请简要描述一下图片" # Please describe the picture in detail
response = model.chat(tokenizer, pixel_values, question, generation_config)
print(f"User: {question}\nAssistant: {response}")
