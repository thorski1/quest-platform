"""
AI Multimodal skill pack — The Perception Lab
Teaches multimodal AI: vision, audio, multimodal models, video & 3D,
and real-world applications like self-driving, medical imaging, and accessibility.
For a general audience, guided by ARIA.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  __  __       _ _   _                 _       _
 |  \/  |_   _| | |_(_)_ __ ___   ___ | |_ ___| |
 | |\/| | | | | | __| | '_ ` _ \ / _ \| __/ _ \ |
 | |  | | |_| | | |_| | | | | | | (_) | ||  __/ |
 |_|  |_|\__,_|_|\__|_|_| |_| |_|\___/ \__\___|_|
"""

SKILL_PACK = SkillPack(
    id="ai_multimodal",
    title="The Perception Lab",
    subtitle="◈  Multimodal AI: Teaching Machines to Perceive the World  ◈",
    save_file_name="ai_multimodal_quest",
    intro_story=INTRO_STORY,
    quit_message="The Perception Lab dims. Your progress is saved — the sensors will still be calibrated when you return.",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Perceiver",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "vision_ai": "visual_cortex_master",
        "audio_ai": "sound_architect",
        "multimodal_models": "fusion_specialist",
        "video_and_3d": "dimension_navigator",
        "real_world_applications": "integration_engineer",
    },
    achievements={
        "visual_cortex_master":  ("Visual Cortex Master", "Mastered image classification, object detection, OCR, segmentation, and vision architectures!"),
        "sound_architect":       ("Sound Architect", "Conquered speech-to-text, TTS, voice cloning, music generation, and real-time audio AI!"),
        "fusion_specialist":     ("Fusion Specialist", "Understood GPT-4V, Gemini, Claude vision, DALL-E, diffusion models, and cross-modal reasoning!"),
        "dimension_navigator":   ("Dimension Navigator", "Explored video understanding, Sora, NeRF, Gaussian splatting, and point clouds!"),
        "integration_engineer":  ("Integration Engineer", "Connected multimodal AI to self-driving, medical imaging, accessibility, and creative tools!"),
        "no_hints":              ("Independent Thinker", "Completed a zone without any hints!"),
        "speed_reader":          ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="neural",
    level_titles=[
        (1, "Novice"),
        (6, "Apprentice"),
        (11, "Practitioner"),
        (16, "Specialist"),
        (21, "Architect"),
        (26, "Master"),
    ],
)
