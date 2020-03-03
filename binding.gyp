{
  "targets": [{
    "target_name": "test-ai-classifier",
    "cflags!": [ "-fno-exceptions" ],
    "cflags_cc!": [ "-fno-exceptions" ],
    "sources": [
      "cc/main.cc",
      "cc/detection.cc"
    ],
    'include_dirs': [
      "<!@(node -p \"require('node-addon-api').include\")",
      "./node_modules/@tensorflow/tfjs-node/deps/include"
    ],
    "libraries": [
      "<(module_root_dir)/node_modules/@tensorflow/tfjs-node/deps/lib/libtensorflow.so.1",
      "<(module_root_dir)/node_modules/@tensorflow/tfjs-node/deps/lib/libtensorflow_framework.so.1",
    ],
    'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ]
  }]
}
