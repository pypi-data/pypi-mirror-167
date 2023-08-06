import logging
from typing import List, Callable, Dict, Any, Type, Tuple
import tensorflow as tf
from tensorflow.keras.layers import BatchNormalization, Concatenate, Layer, Permute, LayerNormalization, Reshape, \
    MultiHeadAttention
from tensorflow.keras.layers.experimental import SyncBatchNormalization
from tensorflow.keras.layers.experimental.preprocessing import Normalization
from tensorflow_addons.layers import InstanceNormalization, GroupNormalization
from keras.saving.saved_model.load import RevivedLayer
from keras_data_format_converter.layers.confighandlers.axischange import handle_axis_change
from keras_data_format_converter.layers.confighandlers.dataformat import handle_data_format
from keras_data_format_converter.layers.confighandlers.dims import handle_transpose_dims
from keras_data_format_converter.layers.confighandlers.targetshape import handle_transpose_target_shape

HandlerType = Callable[[str, Dict[str, Any]], Dict[str, Any]]
layer_to_config_handlers: Dict[Type[Layer], List[HandlerType]] = {
    BatchNormalization: [handle_axis_change],
    LayerNormalization: [handle_axis_change],
    GroupNormalization: [handle_axis_change],
    InstanceNormalization: [handle_axis_change],
    SyncBatchNormalization: [handle_axis_change],
    Normalization: [handle_axis_change],
    Concatenate: [handle_axis_change],
    Permute: [handle_transpose_dims],
    Reshape: [handle_transpose_target_shape]
}


def convert_layer(current_layer: Layer, target_data_format: str, input_shape: List[int], transform_signal: bool,
                  custom_layers: Dict[str, Type[tf.keras.layers.Layer]]) \
        -> Tuple[Layer, bool]:
    logger = logging.getLogger(__name__)
    config = current_layer.get_config()

    if isinstance(current_layer, RevivedLayer):
        logger.debug(f"Layer skipped, name: {current_layer.name}, type: {current_layer.__class__.__name__},"
                     f" input_shape: {current_layer.input_shape}, output_shape: {current_layer.output_shape}")
        is_built = True
        return current_layer, is_built

    # handle config changes
    layer_config_handlers = [handle_data_format]
    if transform_signal:
        layer_type = type(current_layer)
        handlers = layer_to_config_handlers.get(layer_type, [])
        layer_config_handlers.extend(handlers)
        if hasattr(current_layer, 'get_special_data_format_handler'):
            special_data_format_handler = current_layer.get_special_data_format_handler()
            layer_config_handlers.append(special_data_format_handler)

    for layer_config_handler in layer_config_handlers:
        logger.debug(f"using config handler, handler name: {layer_config_handler.__name__}")
        config = layer_config_handler(target_data_format, config)

    converted_layer = type(current_layer).from_config(config)
    is_built = True
    if isinstance(current_layer, MultiHeadAttention) or isinstance(current_layer, tuple(custom_layers.values())):
        is_built = False
        return converted_layer, is_built

    weights = current_layer.get_weights()
    converted_layer.build(input_shape)
    converted_layer.set_weights(weights)
    logger.debug(f"Layer created, name: {converted_layer.name}, type: {current_layer.__class__.__name__},"
                 f" input_shape: {current_layer.input_shape}, output_shape: {current_layer.output_shape}")
    return converted_layer, is_built
