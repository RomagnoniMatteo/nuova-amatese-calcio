<template>
    <div class="pokeball-loader" aria-label="Caricamento immagine">
        <div class="pokeball">
            <div class="pokeball-top"></div>
            <div class="pokeball-band"></div>
            <div class="pokeball-bottom"></div>
            <div class="pokeball-button"></div>
        </div>
    </div>
</template>

<style scoped>
.pokeball-loader {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
}

.pokeball {
    position: relative;
    width: 56px;
    height: 56px;
    border-radius: 50%;
    background: #f7f3ea;
    border: 3px solid #141414;
    overflow: hidden;
    animation: pokeball-bounce 1s ease-in-out infinite;
}

.pokeball-top {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 50%;
    background: #d64550;
}

.pokeball-bottom {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 50%;
    background: #f7f3ea;
}

.pokeball-band {
    position: absolute;
    top: 50%;
    left: 0;
    width: 100%;
    height: 6px;
    background: #141414;
    transform: translateY(-50%);
}

.pokeball-button {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 16px;
    height: 16px;
    background: #f7f3ea;
    border: 3px solid #141414;
    border-radius: 50%;
    transform: translate(-50%, -50%);
}

@keyframes pokeball-bounce {

    0%,
    100% {
        transform: translateY(0) rotate(0deg);
    }

    50% {
        transform: translateY(-10px) rotate(180deg);
    }
}

@media (prefers-reduced-motion: reduce) {
    .pokeball {
        animation: none;
    }
}
</style>