import tkinter as tk
from tkinter import messagebox
from dataclasses import dataclass
from typing import Callable, Dict, List, Optional, Union


@dataclass
class Line:
    speaker: str
    text: str


@dataclass
class Choice:
    prompt: str
    options: List[Dict[str, str]]  # each: {"text": str, "next": scene_id}


SceneContent = List[Union[Line, Choice]]


class VisualNovelApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Kaique & Caique - Visual Novel")
        self.root.geometry("820x520")
        self.root.configure(bg="#101418")

        # Fonts and colors
        self.fg = "#E6EDF3"
        self.muted = "#9BA3AE"
        self.accent = "#7C9EFF"
        self.bg_panel = "#0B0F14"
        self.bg_button = "#1C232B"

        # Layout: Name box, dialogue box, controls
        top = tk.Frame(self.root, bg=self.bg_panel)
        top.pack(fill=tk.BOTH, expand=True, padx=16, pady=(16, 8))

        self.name_var = tk.StringVar()
        self.name_label = tk.Label(
            top, textvariable=self.name_var, anchor="w",
            font=("Segoe UI", 14, "bold"), fg=self.accent, bg=self.bg_panel
        )
        self.name_label.pack(fill=tk.X)

        self.text = tk.Text(
            top, height=12, wrap=tk.WORD, padx=12, pady=12,
            font=("Segoe UI", 12), fg=self.fg, bg="#121720", bd=0
        )
        self.text.pack(fill=tk.BOTH, expand=True)
        self.text.config(state=tk.DISABLED)

        controls = tk.Frame(self.root, bg=self.root["bg"])  # same as root bg
        controls.pack(fill=tk.X, padx=16, pady=(0, 16))

        self.choice_frame = tk.Frame(controls, bg=self.root["bg"])  # dynamic choices
        self.choice_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.next_btn = tk.Button(
            controls, text="Avançar ▶", command=self.next,
            font=("Segoe UI", 11, "bold"), fg=self.fg, bg=self.bg_button,
            activebackground="#27303A", activeforeground=self.fg,
            relief=tk.FLAT, padx=14, pady=8
        )
        self.next_btn.pack(side=tk.RIGHT)

        # Story engine state
        self.scenes: Dict[str, SceneContent] = self._build_scenes()
        self.current_scene_id: str = "inicio"
        self.line_index: int = 0
        self.waiting_choice: bool = False

        self._render_current()

    # ---------------- UI helpers ----------------
    def _set_dialog(self, speaker: Optional[str], text: str):
        self.name_var.set(speaker or "")
        self.text.config(state=tk.NORMAL)
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, text)
        self.text.config(state=tk.DISABLED)

    def _clear_choices(self):
        for w in list(self.choice_frame.children.values()):
            w.destroy()

    def _show_choice(self, choice: Choice):
        self._clear_choices()
        prompt_lbl = tk.Label(
            self.choice_frame, text=choice.prompt, fg=self.muted,
            bg=self.root["bg"], font=("Segoe UI", 11, "bold")
        )
        prompt_lbl.pack(anchor="w", pady=(0, 6))

        def make_handler(next_scene: str) -> Callable[[], None]:
            def handler():
                self.current_scene_id = next_scene
                self.line_index = 0
                self.waiting_choice = False
                self._clear_choices()
                self._render_current()
            return handler

        for opt in choice.options:
            b = tk.Button(
                self.choice_frame, text=opt["text"], command=make_handler(opt["next"]),
                font=("Segoe UI", 11), fg=self.fg, bg=self.bg_button,
                activebackground="#27303A", activeforeground=self.fg,
                relief=tk.FLAT, padx=10, pady=8
            )
            b.pack(anchor="w", pady=6, fill=tk.X)

        self.waiting_choice = True

    # ---------------- Engine ----------------
    def _build_scenes(self) -> Dict[str, SceneContent]:
        """Define story content here."""
        s: Dict[str, SceneContent] = {}

        s["inicio"] = [
            Line("Narrador", "Quadra do bairro, fim de tarde. O sol aquece a areia. Dois amigos aquecem para o treino de vôlei de praia."),
            Line("Kaique", "Passe curto! Caique, prepara o ataque!"),
            Line("Caique", "Recebido! Levanta que eu explodo essa!"),
            Choice(
                prompt="O treino esquenta e o ritmo sincroniza. O que fazer?",
                options=[
                    {"text": "Focar no treino para o torneio escolar", "next": "treino"},
                    {"text": "Chamar para um açaí depois, conversar com calma", "next": "acai"},
                ],
            ),
        ]

        s["treino"] = [
            Line("Kaique", "Seu saque em salto está muito mais consistente. Eu confio em você no set decisivo."),
            Line("Caique", "E eu confio em você no bloqueio. A gente se completa, né?"),
            Line("Narrador", "Entre risos, algo não dito paira no ar."),
            Choice(
                prompt="No intervalo, aparece a chance de falar sobre sentimentos:",
                options=[
                    {"text": "Kaique abre o coração", "next": "confissao_kaique"},
                    {"text": "Caique toma a iniciativa", "next": "confissao_caique"},
                ],
            ),
        ]

        s["acai"] = [
            Line("Narrador", "No quiosque, o barulho do mar acompanha a conversa."),
            Line("Caique", "Kaique, eu curto demais treinar com você. Não só por ganhar jogo…"),
            Line("Kaique", "Eu também. Com você eu me sinto em casa. Em quadra e fora dela."),
            Choice(
                prompt="Como conduzir a conversa?",
                options=[
                    {"text": "Falar de sonhos e do torneio", "next": "sonhos"},
                    {"text": "Falar do que sente, com carinho", "next": "confissao_caique"},
                ],
            ),
        ]

        s["sonhos"] = [
            Line("Kaique", "Imagina a final, quadra lotada, a gente levantando o troféu."),
            Line("Caique", "E depois?"),
            Line("Kaique", "Depois a gente comemora, juntos. Do jeito que o coração pedir."),
            Choice(
                prompt="O que o coração pede?",
                options=[
                    {"text": "Assumir o sentimento", "next": "confissao_caique"},
                    {"text": "Guardar para depois do torneio", "next": "guardar"},
                ],
            ),
        ]

        s["guardar"] = [
            Line("Narrador", "Eles decidem esperar. O toque de mãos demora um pouco mais do que antes."),
            Line("Caique", "Depois do torneio, então. Mas não deixa eu esquecer, tá?"),
            Line("Kaique", "Eu não vou esquecer."),
            Choice(
                prompt="Chega o dia do torneio. Como jogar?",
                options=[
                    {"text": "Com emoção, pela parceria", "next": "final_feliz"},
                    {"text": "Sob pressão, medo de errar", "next": "final_aprendizado"},
                ],
            ),
        ]

        s["confissao_kaique"] = [
            Line("Kaique", "Caique… eu gosto de você. Não só como dupla."),
            Line("Caique", "Eu senti isso vindo. E… eu gosto de você também."),
            Choice(
                prompt="Como seguir?",
                options=[
                    {"text": "Continuar treinando como casal", "next": "final_feliz"},
                    {"text": "Contar aos amigos primeiro", "next": "amigos"},
                ],
            ),
        ]

        s["confissao_caique"] = [
            Line("Caique", "Kaique, eu te admiro. Seu jeito de me apoiar, de me olhar… eu gosto de você."),
            Line("Kaique", "Eu também gosto de você. Obrigado por dizer.") ,
            Choice(
                prompt="O que fazer agora?",
                options=[
                    {"text": "Treinar juntos, de mãos dadas", "next": "final_feliz"},
                    {"text": "Compartilhar com a galera", "next": "amigos"},
                ],
            ),
        ]

        s["amigos"] = [
            Line("Narrador", "No grupo da escola, rola estranhamento de alguns e apoio de muitos."),
            Line("Kaique", "A gente segue juntos. Na quadra e fora dela."),
            Line("Caique", "E quem respeita, joga com a gente. Quem não, aprende a respeitar."),
            Choice(
                prompt="Dia do torneio:",
                options=[
                    {"text": "Jogar pelo amor e pela parceria", "next": "final_feliz"},
                    {"text": "Lidar com vaias e aprender com isso", "next": "final_aprendizado"},
                ],
            ),
        ]

        s["final_feliz"] = [
            Line("Narrador", "Bloqueio perfeito, defesa na areia, largadinha no fundo. Match point."),
            Line("Caique", "É nosso!"),
            Line("Kaique", "É nosso!"),
            Line("Narrador", "No abraço da vitória, eles encontram espaço para o amor. Pretos, talentosos, e livres para brilhar."),
            Choice(
                prompt="Fim — Jogar novamente?",
                options=[
                    {"text": "Recomeçar", "next": "inicio"},
                ],
            ),
        ]

        s["final_aprendizado"] = [
            Line("Narrador", "A pressão pesa e a final escapa por pouco. Dói, mas não define."),
            Line("Kaique", "A gente aprende. Juntos."),
            Line("Caique", "O amor não depende do placar. Ele fortalece para o próximo jogo."),
            Choice(
                prompt="Fim — Tentar outro caminho?",
                options=[
                    {"text": "Recomeçar", "next": "inicio"},
                ],
            ),
        ]

        return s

    def _render_current(self):
        scene = self.scenes[self.current_scene_id]
        if self.line_index >= len(scene):
            # Safety reset if overflow
            self.line_index = len(scene) - 1

        item = scene[self.line_index]
        if isinstance(item, Line):
            self._set_dialog(item.speaker, item.text)
            self.next_btn.config(state=tk.NORMAL)
        elif isinstance(item, Choice):
            self._set_dialog(None, "")
            self._show_choice(item)
            self.next_btn.config(state=tk.DISABLED)

    def next(self):
        if self.waiting_choice:
            # Ignore next while choosing
            return
        scene = self.scenes[self.current_scene_id]
        self.line_index += 1
        if self.line_index >= len(scene):
            # If end of scene and no choice, loop to start
            self.line_index = len(scene) - 1
            messagebox.showinfo("Fim da cena", "Escolha um caminho para continuar.")
            return
        self._render_current()


def main():
    root = tk.Tk()
    app = VisualNovelApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
