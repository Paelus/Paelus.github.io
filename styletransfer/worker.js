// Neural Style Transfer worker: runs ONNX Runtime Web (WASM) off the main thread,
// so the page never freezes while a style is being computed.
importScripts("https://cdn.jsdelivr.net/npm/onnxruntime-web@1.20.1/dist/ort.min.js");

ort.env.wasm.wasmPaths = "https://cdn.jsdelivr.net/npm/onnxruntime-web@1.20.1/dist/";
ort.env.wasm.numThreads = self.crossOriginIsolated ? Math.min(4, navigator.hardwareConcurrency || 2) : 1;

const sessions = {}; // style name -> InferenceSession (each model is loaded once)

async function getSession(style) {
  if (!sessions[style]) {
    self.postMessage({ type: "status", text: `Loading “${style}” model…` });
    sessions[style] = ort.InferenceSession.create(`models/${style}.onnx`, {
      executionProviders: ["wasm"],
      graphOptimizationLevel: "all",
    });
  }
  return sessions[style];
}

self.onmessage = async (e) => {
  const { id, style, data, width, height } = e.data;
  try {
    const session = await getSession(style);
    self.postMessage({ type: "status", text: `Painting in “${style}” style…` });
    const t0 = performance.now();
    // Input: float32 RGB 0-255, NCHW, no mean subtraction
    const input = new ort.Tensor("float32", data, [1, 3, height, width]);
    const out = await session.run({ [session.inputNames[0]]: input });
    const y = out[session.outputNames[0]];
    const [, , oh, ow] = y.dims;
    const src = y.data, area = ow * oh;
    // Output: clip to 0-255 and convert NCHW -> RGBA pixels
    const rgba = new Uint8ClampedArray(area * 4);
    for (let i = 0; i < area; i++) {
      rgba[4 * i] = src[i];               // Uint8ClampedArray clips to 0..255
      rgba[4 * i + 1] = src[i + area];
      rgba[4 * i + 2] = src[i + 2 * area];
      rgba[4 * i + 3] = 255;
    }
    self.postMessage({ type: "result", id, style, width: ow, height: oh, rgba, ms: performance.now() - t0,
                       threads: ort.env.wasm.numThreads }, [rgba.buffer]);
  } catch (err) {
    delete sessions[style];
    self.postMessage({ type: "error", id, style, message: String(err && err.message || err) });
  }
};
