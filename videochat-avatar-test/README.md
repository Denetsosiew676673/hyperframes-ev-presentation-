# VideoChat / UNILAND host feasibility test

Status: **prepared narration only; talking-head inference NOT executed.** No lipsynchronized MP4 has been generated. This is not an output-quality demonstration of MuseTalk.

Inspected upstream Henry-23/VideoChat at commit303681e on2026-10-26. Its avatar pipeline is pretrained MuseTalk inference over an existing portrait video, with the body/background motions inherited from that video. It is not an instruction-driven full-body presenter generator.

## Prepared asset

`uniland-host-test.mp3` / `.wav`: synthetic English male narrator Kokoro am_michael at0.94 synthesis speed, no voice cloning. `script.txt` contains its words. This audio is suitable input for a future host test; it does not establish mouth accuracy, expression naturalness or inference speed.

## Observed blockers

- No /dev/nvidia* device and no nvidia-smi command in current environment.
- Required MuseTalk, VAE, Whisper, pose and face-parsing weights not present.
- Both attempted model download hosts (huggingface.co and www.modelscope.cn) returned HTTP403 through the connection proxy. No weights downloaded.
- Default system Python lacks Torch, OpenCV, Diffusers and Transformers. The repository pins an older Python/CUDA dependency stack; its README suggests Ubuntu22.04/Python3.10/CUDA12.2.

The source has CPU fallback branches; absence of CUDA alone does not prove CPU inference impossible. However the required weights remain unavailable, and its float16 inference path has not been validated on CPU here. README's8GB/3s and20GB/7s claims are author measurements on A100, not results reproduced in this workspace.

## To complete the actual test

Use an environment with accessible model weights and preferably an NVIDIA GPU, or an already deployed MuseTalk service. Use suitable presenter footage with a clearly visible face, stable lighting, little occlusion and restrained movement. This prepared male voice should be paired with an appropriate presenter; the repository's default three demonstration avatars are women and are not selected as a UNILAND business host.

Run the repository's documented environment/model setup, register the presenter in src/thg.py, and drive it with uniland-host-test.wav. Assess final output for lip closure and consonants, mouth-edge artifacts, face consistency, motion repetition and audio alignment. These checks are pending; none is represented as passed.
