from mindnlp.transformers import AutoTokenizer

from internvl.model.internlm2.configuration_internlm2 import InternLM2Config
from internvl.model.internlm2.tokenization_internlm2 import InternLM2Tokenizer

AutoTokenizer.register(InternLM2Config, slow_tokenizer_class=InternLM2Tokenizer)
