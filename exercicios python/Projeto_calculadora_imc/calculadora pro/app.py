import { createFileRoute } from "@tanstack/react-router";
import { useMemo, useState } from "react";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "Calculadora de IMC — Saúde em segundos" },
      {
        name: "description",
        content:
          "Calcule seu Índice de Massa Corporal (IMC) com classificação visual, faixa saudável e recomendações personalizadas.",
      },
      { property: "og:title", content: "Calculadora de IMC" },
      {
        property: "og:description",
        content: "Descubra seu IMC com classificação, gauge animado e recomendações.",
      },
    ],
  }),
  component: Index,
});

type Categoria = {
  id: string;
  rotulo: string;
  min: number;
  max: number;
  emoji: string;
  cor: string;
  texto: string;
};

const CATEGORIAS: Categoria[] = [
  {
    id: "abaixo",
    rotulo: "Abaixo do peso",
    min: 0,
    max: 18.5,
    emoji: "😔",
    cor: "var(--color-warning)",
    texto:
      "Seu IMC indica peso abaixo do recomendado. Procure uma alimentação rica em nutrientes e considere conversar com um nutricionista.",
  },
  {
    id: "saudavel",
    rotulo: "Peso saudável",
    min: 18.5,
    max: 25,
    emoji: "😊",
    cor: "var(--color-success)",
    texto:
      "Parabéns! Seu IMC está na faixa saudável. Mantenha hábitos equilibrados, atividade física regular e boa hidratação.",
  },
  {
    id: "sobrepeso",
    rotulo: "Sobrepeso",
    min: 25,
    max: 30,
    emoji: "🤨",
    cor: "var(--color-warning)",
    texto:
      "Seu IMC indica sobrepeso. Pequenas mudanças na rotina, como mais movimento e alimentação balanceada, fazem grande diferença.",
  },
  {
    id: "obesidade1",
    rotulo: "Obesidade grau 1",
    min: 30,
    max: 35,
    emoji: "😟",
    cor: "var(--color-warning)",
    texto:
      "Seu IMC indica obesidade grau 1. Vale buscar acompanhamento profissional para um plano de saúde personalizado.",
  },
  {
    id: "obesidade2",
    rotulo: "Obesidade grau 2",
    min: 35,
    max: 40,
    emoji: "😣",
    cor: "var(--color-destructive)",
    texto:
      "Seu IMC indica obesidade grau 2. O acompanhamento médico e nutricional é fortemente recomendado.",
  },
  {
    id: "obesidade3",
    rotulo: "Obesidade grau 3",
    min: 40,
    max: Infinity,
    emoji: "😶‍🌫️",
    cor: "var(--color-destructive)",
    texto:
      "Seu IMC indica obesidade grau 3. Procure orientação médica para cuidar da sua saúde com segurança.",
  },
];

const ESCALA_MIN = 15;
const ESCALA_MAX = 40;

function categoriaPorImc(imc: number): Categoria {
  return CATEGORIAS.find((c) => imc >= c.min && imc < c.max) ?? CATEGORIAS[CATEGORIAS.length - 1];
}

function Gauge({ imc }: { imc: number }) {
  const cat = categoriaPorImc(imc);
  const pct = Math.min(1, Math.max(0, (imc - ESCALA_MIN) / (ESCALA_MAX - ESCALA_MIN)));
  const R = 80;
  const C = Math.PI * R;
  const offset = C * (1 - pct);
  return (
    <div className="relative mx-auto w-full max-w-[260px]">
      <svg viewBox="0 0 200 110" className="w-full">
        <path
          d="M 20 100 A 80 80 0 0 1 180 100"
          fill="none"
          stroke="var(--color-muted)"
          strokeWidth="14"
          strokeLinecap="round"
        />
        <path
          d="M 20 100 A 80 80 0 0 1 180 100"
          fill="none"
          stroke={cat.cor}
          strokeWidth="14"
          strokeLinecap="round"
          strokeDasharray={C}
          strokeDashoffset={offset}
          style={{ transition: "stroke-dashoffset 0.9s cubic-bezier(0.22,1,0.36,1)" }}
        />
      </svg>
      <div className="absolute inset-x-0 bottom-0 flex flex-col items-center">
        <span className="text-5xl font-bold tabular-nums text-foreground">{imc.toFixed(1)}</span>
        <span className="text-sm text-muted-foreground">IMC</span>
      </div>
    </div>
  );
}

function Index() {
  const [peso, setPeso] = useState("");
  const [altura, setAltura] = useState("");
  const [erro, setErro] = useState("");
  const [imc, setImc] = useState<number | null>(null);

  const cat = useMemo(() => (imc !== null ? categoriaPorImc(imc) : null), [imc]);

  function calcular(e: React.FormEvent) {
    e.preventDefault();
    const p = parseFloat(peso.replace(",", "."));
    const a = parseFloat(altura.replace(",", "."));
    if (!Number.isFinite(p) || !Number.isFinite(a) || p <= 0 || a <= 0) {
      setErro("Digite valores válidos para peso e altura!");
      setImc(null);
      return;
    }
    setErro("");
    setImc(p / (a * a));
  }

  return (
    <main className="min-h-screen bg-background px-4 py-10 sm:py-16">
      <div className="mx-auto w-full max-w-xl">
        <header className="mb-8 text-center">
          <div
            className="mx-auto mb-4 flex h-14 w-14 items-center justify-center rounded-2xl text-2xl text-primary-foreground"
            style={{ background: "var(--gradient-hero)" }}
          >
            ⚖️
          </div>
          <h1 className="text-3xl font-bold tracking-tight text-foreground sm:text-4xl">
            Calculadora de IMC
          </h1>
          <p className="mt-2 text-muted-foreground">
            Descubra seu Índice de Massa Corporal e receba recomendações para a sua saúde.
          </p>
        </header>

        <form
          onSubmit={calcular}
          className="rounded-3xl border border-border bg-card p-6 sm:p-8"
          style={{ boxShadow: "var(--shadow-card)" }}
        >
          <div className="grid gap-4 sm:grid-cols-2">
            <label className="block">
              <span className="mb-1.5 block text-sm font-medium text-foreground">Peso (kg)</span>
              <input
                inputMode="decimal"
                value={peso}
                onChange={(e) => setPeso(e.target.value)}
                placeholder="Ex: 70"
                className="w-full rounded-xl border border-input bg-background px-4 py-3 text-foreground outline-none transition focus:border-ring focus:ring-2 focus:ring-ring/30"
              />
            </label>
            <label className="block">
              <span className="mb-1.5 block text-sm font-medium text-foreground">Altura (m)</span>
              <input
                inputMode="decimal"
                value={altura}
                onChange={(e) => setAltura(e.target.value)}
                placeholder="Ex: 1.75"
                className="w-full rounded-xl border border-input bg-background px-4 py-3 text-foreground outline-none transition focus:border-ring focus:ring-2 focus:ring-ring/30"
              />
            </label>
          </div>

          <button
            type="submit"
            className="mt-6 w-full rounded-xl px-4 py-3 font-semibold text-primary-foreground transition hover:opacity-90 active:scale-[0.99]"
            style={{ background: "var(--gradient-hero)", boxShadow: "var(--shadow-soft)" }}
          >
            Calcular IMC
          </button>

          {erro && (
            <p className="mt-4 rounded-xl bg-destructive/10 px-4 py-3 text-sm font-medium text-destructive">
              {erro}
            </p>
          )}
        </form>

        {imc !== null && cat && (
          <section
            className="animate-fade-up mt-6 rounded-3xl border border-border bg-card p-6 sm:p-8"
            style={{ boxShadow: "var(--shadow-card)" }}
          >
            <Gauge imc={imc} />

            <div className="mt-4 flex items-center justify-center gap-2 text-center">
              <span className="text-2xl">{cat.emoji}</span>
              <span
                className="rounded-full px-3 py-1 text-sm font-semibold text-primary-foreground"
                style={{ background: cat.cor }}
              >
                {cat.rotulo}
              </span>
            </div>

            <p className="mt-4 text-center text-muted-foreground">{cat.texto}</p>

            <div className="mt-6 space-y-2">
              {CATEGORIAS.map((c) => {
                const ativo = c.id === cat.id;
                return (
                  <div
                    key={c.id}
                    className={`flex items-center justify-between rounded-xl border px-4 py-2.5 text-sm transition ${
                      ativo ? "border-transparent" : "border-border bg-background"
                    }`}
                    style={ativo ? { background: `${c.cor}`, color: "var(--color-primary-foreground)" } : undefined}
                  >
                    <span className="font-medium">
                      {c.emoji} {c.rotulo}
                    </span>
                    <span className="tabular-nums opacity-80">
                      {c.min}{c.max === Infinity ? "+" : `–${c.max}`}
                    </span>
                  </div>
                );
              })}
            </div>

            <p className="mt-6 text-center text-xs text-muted-foreground">
              O IMC é um indicador geral e não substitui avaliação médica profissional.
            </p>
          </section>
        )}
      </div>
    </main>
  );
}
