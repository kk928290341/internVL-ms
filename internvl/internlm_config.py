from internvl.intern_vit_config import InternVisionConfig
from internvl.llm.configs import convert_mstype, BaseConfig


class InternLM2Config(BaseConfig):
    def __init__(
        self,
        batch_size: int = 1,
        seq_length: int = 2048,
        hidden_size: int = 4096,
        num_layers: int = 32,
        num_heads: int = 32,
        n_kv_heads: int = None,
        max_position_embedding: int = None,
        intermediate_size: int = None,
        vocab_size: int = 32000,  # defined later by tokenizer
        multiple_of: int = 256,  # make SwiGLU hidden layer size multiple of large power of 2
        ffn_dim_multiplier: int = None,
        rms_norm_eps: float = 1e-5,
        bos_token_id: int = 1,
        eos_token_id: int = 2,
        pad_token_id: int = 0,
        ignore_token_id: int = -100,
        theta: float = 10000.0,
        compute_dtype: str = "float16",
        layernorm_compute_type: str = "float32",
        softmax_compute_type: str = "float32",
        rotary_dtype: str = "float32",
        param_init_type: str = "float16",
        ln_param_init_type: str = "float32",
        qkv_has_bias: bool = False,
        qkv_concat: bool = False,
        use_past: bool = False,
        pretrain_seqlen=None,
        extend_method: str = "None",
        scaling_factor: float = 1.0,
        is_dynamic: bool = False,
        use_kvcache_op: bool = False,
        is_flexible_shape: bool = False,
        use_rope_slice: bool = False,
        use_flash_attention: bool = False,
        use_paged_attention: bool = False,
        fine_grain_interleave: int = 1,
        offset: int = 0,
        checkpoint_name_or_path: str = "",
        repetition_penalty: float = 1.0,
        max_decode_length: int = 1024,
        block_size: int = 16,
        num_blocks: int = 512,
        top_k: int = 5,
        top_p: float = 1.0,
        do_sample: bool = True,
        **kwargs,
    ):
        super(InternLM2Config, self).__init__(**kwargs)
        self.batch_size = batch_size
        self.seq_length = seq_length
        self.vocab_size = vocab_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.num_heads = num_heads
        self.max_position_embedding = max_position_embedding if max_position_embedding else seq_length
        self.intermediate_size = intermediate_size
        self.multiple_of = multiple_of
        self.n_kv_heads = n_kv_heads
        self.ffn_dim_multiplier = ffn_dim_multiplier
        self.rms_norm_eps = rms_norm_eps
        self.qkv_concat = qkv_concat
        self.param_init_type = convert_mstype(param_init_type)
        self.qkv_has_bias = qkv_has_bias
        self.layernorm_compute_type = convert_mstype(layernorm_compute_type)
        self.softmax_compute_type = convert_mstype(softmax_compute_type)
        self.rotary_dtype = convert_mstype(rotary_dtype)
        self.compute_dtype = convert_mstype(compute_dtype)
        self.ln_param_init_type = convert_mstype(ln_param_init_type)
        self.checkpoint_name_or_path = checkpoint_name_or_path
        self.bos_token_id = bos_token_id
        self.eos_token_id = eos_token_id
        self.pad_token_id = pad_token_id
        self.ignore_token_id = ignore_token_id
        self.use_past = use_past
        self.pretrain_seqlen = pretrain_seqlen
        self.extend_method = extend_method
        self.scaling_factor = scaling_factor
        self.is_dynamic = is_dynamic
        self.use_kvcache_op = use_kvcache_op
        self.is_flexible_shape = is_flexible_shape
        self.use_rope_slice = use_rope_slice
        self.use_flash_attention = use_flash_attention
        self.fine_grain_interleave = fine_grain_interleave
        self.offset = offset
        self.repetition_penalty = repetition_penalty
        self.max_decode_length = max_decode_length
        self.top_k = top_k
        self.top_p = top_p
        self.do_sample = do_sample
        self.theta = theta
        self.use_paged_attention = use_paged_attention
        self.block_size = block_size
        self.num_blocks = num_blocks


class InternVLChatConfig(BaseConfig):
    def __init__(self,
                 vision_model,
                 llm_model,
                 downsample_ratio,
                 template = "internlm2-chat",

                 **kwargs):
        super().__init__(**kwargs)
        assert vision_model is not None
        assert llm_model is not None

        self.vision_config = InternVisionConfig(**vision_model)
        self.llm_config = InternLM2Config(**llm_model)
        self.downsample_ratio = downsample_ratio
        self.template = template
