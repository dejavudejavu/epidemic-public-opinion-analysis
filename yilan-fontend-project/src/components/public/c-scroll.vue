<template>
    <div ref="scroll" class="v-scroll">
        <slot name="main"></slot>
    </div>
</template>

<script>
import PerfectScrollbar from 'perfect-scrollbar'
export default {
    props: {
        state: {
            type: Boolean,
            default: false
        }
    },
    data() {
        return {
            ps: null,
        };
    },
    mounted() {
        const container = this.$refs["scroll"];
        this.ps = new PerfectScrollbar(container, {
            wheelSpeed: 0.5,
            wheelPropagation: true,
            minScrollbarLength: 1,
        });
        container.addEventListener('ps-scroll-y', () => {
            if (!this.state) return false;
            this.$emit("add", 1); 
        });

        setTimeout(() => {
            this.ps.update();
        }, 200);
    },
    methods: {
        update() {
            this.ps.update();
        },
        destroy() {
            this.ps.destroy();
            this.ps = null;
        },
        updateTop() {
            this.$refs["scroll"].scrollTop = 0;
            this.update();
        },
        updateTopEvent(top) {
            this.$refs["scroll"].scrollTop = top;
            this.update();
        } 
    }
}
</script>

<style>

</style>
